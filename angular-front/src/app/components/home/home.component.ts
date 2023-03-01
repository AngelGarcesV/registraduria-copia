import { Component, OnInit } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  constructor(private cookieService: CookieService, private route: Router) {}
  access = 0;
  usuarioData: any = {
    rol: 0,
  };
  ngOnInit(): void {
    //determinar el tipo de acceso actual quemado en codigo
    this.access = 0;
    if (this.cookieService.get('type') == 'admin') {
      this.usuarioData.rol = 'admin';
      this.access = 1;
    } else if (this.cookieService.get('type') == 'jurado') {
      this.usuarioData.rol = 'jurado';
      this.access = 2;
    } else {
      this.access = 0;
    }
  }
}
