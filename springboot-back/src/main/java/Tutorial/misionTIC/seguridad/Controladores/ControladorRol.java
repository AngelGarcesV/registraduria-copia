package Tutorial.misionTIC.seguridad.Controladores;
import Tutorial.misionTIC.seguridad.Modelos.PermisosRoles;
import Tutorial.misionTIC.seguridad.Repositorios.RepositorioPermisosRoles;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import Tutorial.misionTIC.seguridad.Modelos.Rol;
import Tutorial.misionTIC.seguridad.Repositorios.RepositorioRol;
import org.springframework.web.server.ResponseStatusException;


import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/roles")
public class    ControladorRol {
    @Autowired
    private RepositorioRol miRepositorioRol;
    @Autowired
    private RepositorioPermisosRoles miRepositorioPermisoRoles;

    @GetMapping("")
    public List<Rol> index(){
        return this.miRepositorioRol.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Rol create(@RequestBody  Rol infoRol){
        if (infoRol.isValid()){
            return this.miRepositorioRol.save(infoRol);
        }
        throw new ResponseStatusException(HttpStatus.ACCEPTED,"El rol no cumple con los requisitos");

    }
    @GetMapping("{id}")
    public Rol show(@PathVariable String id){
        Rol rolActual=this.miRepositorioRol
                .findById(id)
                .orElse(null);
        return rolActual;
    }
    @PutMapping("{id}")
    public Rol update(@PathVariable String id,@RequestBody  Rol infoRol){
        Rol rolActual=this.miRepositorioRol
                .findById(id)
                .orElse(null);
        if (rolActual!=null){
            rolActual.setNombre(infoRol.getNombre());
            return this.miRepositorioRol.save(rolActual);
        }else{
            return  null;
        }
    }

    @DeleteMapping("{id}")
    public Rol  delete(@PathVariable String id){
        Rol rolActual=this.miRepositorioRol
                .findById(id)
                .orElse(null);
        List<PermisosRoles> permisosRoles=miRepositorioPermisoRoles.getPermisosRol(id);

        if(permisosRoles.isEmpty()){
            if (rolActual!=null){
                this.miRepositorioRol.delete(rolActual);
                return rolActual;
            }else {
                throw new ResponseStatusException(HttpStatus.CONFLICT,"El rol no existe");
            }
        }else {
            throw new ResponseStatusException(HttpStatus.CONFLICT,"No se pudo elimianar debido a que tiene permisos asociaciados");
        }

    }
}
