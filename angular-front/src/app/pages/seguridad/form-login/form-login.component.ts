import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import { LiveAnnouncer } from '@angular/cdk/a11y';
import { LoginService } from 'src/app/services/login.service';
import { EventListenerService } from 'src/app/services/event-listener.service';

@Component({
  selector: 'app-form-login',
  templateUrl: './form-login.component.html',
  styleUrls: ['./form-login.component.scss'],
})
export class FormLoginComponent implements OnInit {
  public loading: boolean = false;
  public err: boolean = false;
  // Inputs.

  constructor(
    private cookieService: CookieService,
    private route: Router,
    private login: LoginService,
    private _liveAnnouncer: LiveAnnouncer,
    private sendDataModule: EventListenerService
  ) {}
  form = {
    email: '',
    password: '',
  };
  submitLogin() {
    this.loading = true;
    this.login.logAndGetType(this.form.email, this.form.password).subscribe(
      (res: any) => {
        console.log(res);
        this.cookieService.set(
          'type',
          res.permisos[0].rol.nombre.toLowerCase()
        );
        this.cookieService.set('userId', res.user_id);
        this.cookieService.set('token', res.token);
        this.sendDataModule.setLogged.emit(true);
        this.sendDataModule.formLog.emit(false);

        this.loading = false;
        this.route.navigate(['/home']);
      },
      (err: any) => {
        console.log(err.status);
        this.err = true;
        this.loading = false;
      }
    );

    /*       if (this.form.email == 'a@a.com' && this.form.password == '123') {
      console.log('Login correcto');
      this.cookieService.set('type', 'admin');
      this.sendDataModule.setLogged.emit(true);
      this.sendDataModule.formLog.emit(false);
      this.route.navigate(['/home']);
    } else if (this.form.email == 'b@b.com' && this.form.password == '123') {
      console.log('Login correcto');
      this.cookieService.set('type', 'jurado');
      this.sendDataModule.setLogged.emit(true);
      this.sendDataModule.formLog.emit(false);
      this.route.navigate(['/home']);
    } else {
      console.log('Login incorrecto');
      this.sendDataModule.setLogged.emit(false);
      this.sendDataModule.formLog.emit(false);
    }
    console.log(this.form.email + ' ' + this.form.password);  */
  }

  ngOnInit(): void {}
}
