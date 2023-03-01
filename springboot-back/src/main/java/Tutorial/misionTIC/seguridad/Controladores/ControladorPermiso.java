package Tutorial.misionTIC.seguridad.Controladores;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import Tutorial.misionTIC.seguridad.Modelos.Permiso;
import Tutorial.misionTIC.seguridad.Repositorios.RepositorioPermiso;
import org.springframework.web.server.ResponseStatusException;


import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos")
public class ControladorPermiso {
    @Autowired
    private RepositorioPermiso miRepositorioPermiso;

    @GetMapping("")
    public List<Permiso> index(){
        return this.miRepositorioPermiso.findAll();
    }
    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Permiso create(@RequestBody  Permiso infoPermiso){

        System.out.println(infoPermiso);

        Permiso permiso=miRepositorioPermiso.getPermiso(infoPermiso.getUrl(),infoPermiso.getMetodo());

        System.out.println(permiso);

        if(permiso == null){
            if (infoPermiso.isValid()){
                return this.miRepositorioPermiso.save(infoPermiso);
            }
        }else {
            throw new ResponseStatusException(HttpStatus.ACCEPTED,"Ya existe el permiso");
        }


        throw new ResponseStatusException(HttpStatus.ACCEPTED,"El permiso no cumple con los requisitos");

    }
    @GetMapping("{id}")
    public Permiso show(@PathVariable String id){
        Permiso permisoActual=this.miRepositorioPermiso
                .findById(id)
                .orElse(null);
        return permisoActual;
    }
    @PutMapping("{id}")
    public Permiso update(@PathVariable String id,@RequestBody  Permiso infoPermiso){
        Permiso permisoActual=this.miRepositorioPermiso
                .findById(id)
                .orElse(null);
        if(permisoActual!=null){
            permisoActual.setMetodo(infoPermiso.getMetodo());
            permisoActual.setUrl(infoPermiso.getUrl());
            return this.miRepositorioPermiso.save(permisoActual);
        }else{
            return null;
        }

    }

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Permiso permisoActual=this.miRepositorioPermiso
                .findById(id)
                .orElse(null);
        if (permisoActual!=null){
            this.miRepositorioPermiso.delete(permisoActual);
        }
    }
}