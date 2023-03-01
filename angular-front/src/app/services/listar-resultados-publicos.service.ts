import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class ListarResultadosPublicosService {
  API = 'http://127.0.0.1:5000'; //link del backend, SOLO para resultados
  url = 'https://jsonplaceholder.typicode.com/users'; //link SOLO PARA PRUEBAS

  endpoints = {
    //objeto con los endpoints de los resultados
    candidato: `${this.API}/getresultbycandidate`,
    mesas: `${this.API}/getResultbyTable`,
    partido: `${this.API}/getResultbyParty`,
    congreso: `${this.API}/getNewCongress`,
    resultados: `${this.API}/getallresult`,
  };
  constructor(private http: HttpClient) {
    console.log('servicio ejecutado');
  }
  //getResults recibe un parametro que es el llamado al tipo de resultado que se quiere obtener
  getResultados(type: string) {
    //funcion que retorna los resultados de la API segun la pagina donde se encuentre
    // Esta funcion se utiliza en el componente de resultados /components/dynamic-table
    if (type == 'partido') {
      return this.http.get(this.endpoints.partido);
    } else if (type == 'mesas') {
      return this.http.get(this.endpoints.mesas);
    } else if (type == 'candidato') {
      return this.http.get(this.endpoints.candidato);
    } else if (type == 'resultados') {
      return this.http.get(this.endpoints.resultados);
    } else if (type == 'congreso') {
      return this.http.get(this.endpoints.congreso);
    } else {
      return this.http.get(this.url);
    }
  }
}
