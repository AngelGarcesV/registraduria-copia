import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import { EventListenerService } from 'src/app/services/event-listener.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent implements OnInit {
  constructor(private cookieService: CookieService, private route: Router,
    private sendDataModule : EventListenerService) {}
  @Input() logged = false;
  //Outputs


  isActiveOrLogged(){
    return this.logged || this.cookieService.get("token") != ""
  }

  submitLogin() {
    this.sendDataModule.formLog.emit(true);
    this.route.navigate(['/seguridad/login']);
  }

  submitClose() {
    this.cookieService.deleteAll();
    this.sendDataModule.setLogged.emit(false);
    this.sendDataModule.formLog.emit(false);
    this.route.navigate(['/']);
  }

  inicio() {
    this.route.navigate(['/home']);
  }
  ngOnInit(): void {
    this.sendDataModule.setLogged.subscribe(data =>{
      this.logged = data;
    })

  }
}
