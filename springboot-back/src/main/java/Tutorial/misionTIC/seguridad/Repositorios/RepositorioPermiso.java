package Tutorial.misionTIC.seguridad.Repositorios;
import Tutorial.misionTIC.seguridad.Modelos.Permiso;
import Tutorial.misionTIC.seguridad.Modelos.PermisosRoles;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.List;


public interface RepositorioPermiso extends MongoRepository<Permiso,String> {

    @Query("{$and :[{'url':{$eq:?0}},{'metodo':{$eq:?1}}]}")
    public Permiso getPermiso(String url,String metodo);
}
