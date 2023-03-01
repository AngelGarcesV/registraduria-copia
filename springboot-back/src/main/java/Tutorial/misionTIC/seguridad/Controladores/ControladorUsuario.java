package Tutorial.misionTIC.seguridad.Controladores;
import Tutorial.misionTIC.seguridad.Modelos.Usuario;
import Tutorial.misionTIC.seguridad.Modelos.Rol;
import Tutorial.misionTIC.seguridad.Repositorios.RepositorioUsuario;
import Tutorial.misionTIC.seguridad.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

@CrossOrigin
@RestController
@RequestMapping("/usuarios")
public class ControladorUsuario {
    @Autowired
    private RepositorioUsuario miRepositorioUsuario;
    @Autowired
    private RepositorioRol miRepositorioRol;

    @GetMapping("")
    public List<Usuario> index(){
        System.out.println("solicitud de users");
        return this.miRepositorioUsuario.findAll();
    }
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Usuario create(@RequestBody  Usuario infoUsuario){
        if (infoUsuario.isValid()){
            Usuario usuarioActual=this.miRepositorioUsuario.getUserByEmail(infoUsuario.getCorreo());
            if(usuarioActual==null){
                infoUsuario.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
                return this.miRepositorioUsuario.save(infoUsuario);
            }else {
                throw new ResponseStatusException(HttpStatus.ACCEPTED,"El correo ya existe ");
            }


        }
        throw new ResponseStatusException(HttpStatus.ACCEPTED,"El usuario no cumple con los requisitos");


    }
    @GetMapping("{id}")
    public Usuario show(@PathVariable String id){

        Usuario usuarioActual=this.miRepositorioUsuario.findById(id).orElse(null);
        if(usuarioActual==null){
            throw new ResponseStatusException(HttpStatus.ACCEPTED,"El usuario no fue ecnontrado");
        }
        return usuarioActual;
    }
    @PutMapping("{id}")
    public Usuario update(@PathVariable String id,@RequestBody  Usuario infoUsuario){
        Usuario usuarioActual=this.miRepositorioUsuario.findById(id).orElse(null);

        if (usuarioActual!=null){
            Usuario usuarioCorreo=this.miRepositorioUsuario.getUserByEmail(infoUsuario.getCorreo());
            if(usuarioCorreo == null){
                usuarioActual.setSeudonimo(infoUsuario.getSeudonimo());
                usuarioActual.setCorreo(infoUsuario.getCorreo());
                usuarioActual.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
                return this.miRepositorioUsuario.save(usuarioActual);
            }else {
                throw new ResponseStatusException(HttpStatus.ACCEPTED,"El correo ya existe ");
            }

        }else{
            return null;
        }
    }

    @DeleteMapping("{id}")
    public Usuario   delete(@PathVariable String id){
        Usuario usuarioActual=this.miRepositorioUsuario
                .findById(id)
                .orElse(null);
        System.out.println("borrando"+usuarioActual);
        if (usuarioActual!=null){
            this.miRepositorioUsuario.delete(usuarioActual);
            return usuarioActual;
        }else {
            throw new ResponseStatusException(HttpStatus.ACCEPTED,"El usuario no existe ");

        }



    }

    /**
     * Relación (1 a n) entre rol y usuario
     * @param id
     * @param id_rol
     * @return
     */
    @PutMapping("{id}/rol/{id_rol}")
    public Usuario asignarRolAUsuario(@PathVariable String id,@PathVariable String id_rol){
        Usuario usuarioActual=this.miRepositorioUsuario
                .findById(id)
                .orElse(null);
        if(usuarioActual==null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND,"El usuario solicitado no existe");
        }
        Rol rolActual=this.miRepositorioRol
                .findById(id_rol)
                .orElse(null);
        if(rolActual==null){
            throw new ResponseStatusException(HttpStatus.NOT_FOUND,"El rol solicitado no existe");
        }

        usuarioActual.setRol(rolActual);
        return this.miRepositorioUsuario.save(usuarioActual);


    }

    public String convertirSHA256(String password) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
        }
        catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for(byte b : hash) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }


    @PostMapping("/validar")
    public Usuario validate(@RequestBody  Usuario infoUsuario,
                            final HttpServletResponse response) throws IOException {
        Usuario usuarioActual=this.miRepositorioUsuario
                .getUserByEmail(infoUsuario.getCorreo());
        if (usuarioActual!=null &&
                usuarioActual.getContrasena().equals(convertirSHA256(infoUsuario.getContrasena()))) {
            usuarioActual.setContrasena("");
            return usuarioActual;
        }else{
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }
}