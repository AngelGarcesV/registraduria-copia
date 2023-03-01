import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import Swal from 'sweetalert2';

@Injectable({
  providedIn: 'root',
})
export class JuradoServiceService {
  API = 'http://127.0.0.1:7777';
  API2 = 'http://127.0.0.1:5000';

  endpoints = {
    //objeto con los endpoints de los resultados
    getCandidates: `${this.API2}/getallcandidate`,
    createResult: `${this.API2}/createresult`,
  };
  constructor(private http: HttpClient) {
    console.log('servicio ejecutado');
  }

  getDataCandidate() {
    return this.http.get(this.endpoints.getCandidates);
  }

  createResult(data: any) {
    return this.http.post(this.endpoints.createResult, data);
  }

  sendNotification() {
    Swal.fire('Voto agregado exitosamente', '', 'success');
  }
}
