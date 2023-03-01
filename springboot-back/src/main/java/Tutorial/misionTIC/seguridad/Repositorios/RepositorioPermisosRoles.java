package Tutorial.misionTIC.seguridad.Repositorios;
import Tutorial.misionTIC.seguridad.Modelos.Permiso;
import Tutorial.misionTIC.seguridad.Modelos.PermisosRoles;
import Tutorial.misionTIC.seguridad.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.List;


public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String>
{
    @Query("{'rol': ?0}")
    public List<PermisosRoles> getPermisosRol(String id);

    @Query("{$and :[{'rol':{$eq:?0}},{'permiso':{$eq:?1}}]}")
    public PermisosRoles getPermisoRolByRolPermiso(String idRol, String idPermiso);
}

