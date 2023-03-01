package Tutorial.misionTIC.seguridad.Controladores;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import Tutorial.misionTIC.seguridad.Modelos.Permiso;
import Tutorial.misionTIC.seguridad.Modelos.PermisosRoles;
import Tutorial.misionTIC.seguridad.Modelos.Rol;
import Tutorial.misionTIC.seguridad.Repositorios.RepositorioPermiso;
import Tutorial.misionTIC.seguridad.Repositorios.RepositorioPermisosRoles;
import Tutorial.misionTIC.seguridad.Repositorios.RepositorioRol;
import org.springframework.web.server.ResponseStatusException;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;
import java.util.concurrent.atomic.AtomicReference;

@CrossOrigin
@RestController
@RequestMapping("/permisos-roles")
public class ControladorPermisosRoles {
    @Autowired
    private RepositorioPermisosRoles miRepositorioPermisoRoles;

    @Autowired
    private RepositorioPermiso miRepositorioPermiso;

    @Autowired
    private RepositorioRol miRepositorioRol;



    @GetMapping("")
    public List<PermisosRoles> index(){
        return this.miRepositorioPermisoRoles.findAll();
    }

    /**
     * Asignación rol y permiso
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRoles create(@PathVariable String id_rol,@PathVariable String id_permiso){
        System.out.println("creado permiso rol");
        PermisosRoles nuevo=new PermisosRoles();
        PermisosRoles decomprobacion=miRepositorioPermisoRoles.getPermisoRolByRolPermiso(id_rol,id_permiso);
        if(decomprobacion == null){
            Rol elRol=this.miRepositorioRol.findById(id_rol).get();
            Permiso elPermiso=this.miRepositorioPermiso.findById(id_permiso).get();

            if (elRol!=null && elPermiso!=null){
                nuevo.setPermiso(elPermiso);
                nuevo.setRol(elRol);
                return this.miRepositorioPermisoRoles.save(nuevo);
            }else{
                return null;
            }
        }else {
            throw new ResponseStatusException(HttpStatus.ALREADY_REPORTED,"Este permiso ya le ha sido asignado");
        }

    }

    @GetMapping("{id}")
    public PermisosRoles show(@PathVariable String id){
        PermisosRoles permisosRolesActual=this.miRepositorioPermisoRoles
                .findById(id)
                .orElse(null);
        return permisosRolesActual;
    }
   @GetMapping("/permisos/{id}")
    public List<PermisosRoles> getPermisos(@PathVariable String id){
        List<PermisosRoles> permisos=this.miRepositorioPermisoRoles.getPermisosRol(id);
        System.out.println(permisos );
        return permisos;
    }
    /**
     * Modificación Rol y Permiso
     * @param id
     * @param id_rol
     * @param id_permiso
     * @return
     */
    @PutMapping("{id}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRoles update(@PathVariable String id,@PathVariable String id_rol,@PathVariable String id_permiso){
        PermisosRoles permisosRolesActual=this.miRepositorioPermisoRoles
                .findById(id)
                .orElse(null);
        Rol elRol=this.miRepositorioRol.findById(id_rol).orElse(null);
        Permiso elPermiso=this.miRepositorioPermiso.findById(id_permiso).get();
        if(permisosRolesActual!=null && elPermiso!=null && elRol!=null){
            permisosRolesActual.setPermiso(elPermiso);
            permisosRolesActual.setRol(elRol);

            return this.miRepositorioPermisoRoles.save(permisosRolesActual);
        }else{
            return null;
        }
    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        PermisosRoles permisosRolesActual=this.miRepositorioPermisoRoles.findById(id).orElse(null);

        if (permisosRolesActual!=null){
            this.miRepositorioPermisoRoles.delete(permisosRolesActual);
        }
    }


    @GetMapping("/validar-permiso/rol/{id}")
    public PermisosRoles validate(@PathVariable String id,@RequestBody  Permiso permiso,final HttpServletResponse response) throws IOException {


        List<PermisosRoles> permisosRoles = this.miRepositorioPermisoRoles.getPermisosRol(id);

        System.out.println(permiso);

        PermisosRoles tienePermiso= null;

        for( int i=0;i<permisosRoles.size();i++){
            if(permisosRoles.get(i).getPermiso().getMetodo().equals(permiso.getMetodo()) & permisosRoles.get(i).getPermiso().getUrl().equals(permiso.getUrl())){

                tienePermiso=permisosRoles.get(i);

                break;
            }
        }

        System.out.println(permisosRoles);

        System.out.println(tienePermiso);
        return tienePermiso;
    }
    }
