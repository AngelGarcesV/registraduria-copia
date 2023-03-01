package Tutorial.misionTIC.seguridad.Modelos;
import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;
@Data
@Document()
public class Usuario {
    @Id
    private String _id;
    private String seudonimo;
    private String correo;
    private String contrasena;
//pruebaaa
    private String mesa;
    @DBRef
    private Rol rol;

    public Rol getRol() {
        return rol;
    }

    public void setRol(Rol rol) {
        this.rol = rol;
    }

    public Usuario(String seudonimo, String correo, String contrasena, String mesa) {
        this.seudonimo = seudonimo;
        this.correo = correo;
        this.contrasena = contrasena;
        this.mesa = mesa;
    }

    public String get_id() {
        return _id;
    }

    public Boolean isValid(){
        if (this.correo==null || this.seudonimo==null || this.contrasena==null)
        {
            return false;
        }
        return true;
    }



    public String getSeudonimo() {
        return seudonimo;
    }

    public void setSeudonimo(String seudonimo) {
        this.seudonimo = seudonimo;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getContrasena() {
        return contrasena;
    }

    public void setContrasena(String contrasena) {
        this.contrasena = contrasena;
    }


    public String getMesa(){
        return mesa;
    }


    public void setMesa(String mesa){
        this.mesa = mesa;
    }
}