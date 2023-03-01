import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service'; // <-- import the CookieService
import { Router } from '@angular/router'; // <-- import the Router
import { EventListenerService } from './services/event-listener.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  title = 'registaduria-app';
  logged = false; //determina si ya hizo proceso de loguin
  formLog = false; //Comprueba si abrio el formulario de login para mostrar UNICAMENTE el formulario
  constructor(
    private cookieService: CookieService,
    private router: Router,
    private sendDataModule: EventListenerService
  ) {} // <-- inject the CookieService and Router
  ngOnInit(): void {
    // ngInit es el equivalente a useEffect en react
    const typeUser = this.cookieService.get('type');
    if (typeUser == 'admin' || typeUser == 'jurado') {
      this.logged = true; // determina si esta o no logueado
    }
    this.sendDataModule.formLog.subscribe((data) => {
      this.formLog = data;
    });
    this.sendDataModule.setLogged.subscribe((data) => {
      this.logged = data;
    });
  }

  isHome() {
    //Lo uso para que no se repita la impresion en el html, ya que el router-outlet se repite en todas las paginas
    return this.router.url === '/';
  }

  isLogged() {
    //Determina si esta logueado o no, para mostrar el menu de navegacion
    return this.logged;
  }

  loggedUser(respuesta: any) {
    //Envia al componente padre el estado de logueo
    this.logged = respuesta;
  }
  formLogged(respuesta: any) {
    //Envia al componente padre si esta en el formulario de login
    this.formLog = respuesta;
  }
}
