import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class LoginService {
  API = 'http://127.0.0.1:7777';

  endpoints = {
    //objeto con los endpoints de los resultados
    login: `${this.API}/login`,
    getTable: `${this.API}/usuarios/`,
  };

  constructor(private http: HttpClient) {
    console.log('servicio ejecutado');
  }

  logAndGetType(email: string, password: string) {
    return this.http.post(this.endpoints.login, {
      correo: email,
      contrasena: password,
    });
  }

  getTable(id: any, token: any) {
    const headers = new HttpHeaders().set('Authorization', 'Bearer ' + token);
    return this.http.get(this.endpoints.getTable + `${id}`, { headers });
  }

  printable(a: any, b: any) {
    console.log(a, b);
  }
}
