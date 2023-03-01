import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { CookieService } from 'ngx-cookie-service';
import { FormsModule } from '@angular/forms';
import { MatSortModule } from '@angular/material/sort';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';
import { HttpClientModule } from '@angular/common/http';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatPaginatorModule } from '@angular/material/paginator';
import { NgChartsModule } from 'ng2-charts';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormLoginComponent } from './pages/seguridad/form-login/form-login.component';
import { HomeComponent } from './components/home/home.component';
import { HeaderComponent } from './components/header/header.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { TestComponent } from './pages/test/test.component';
import { ResultsMenuComponent } from './pages/resultados/results-menu/results-menu.component';
import { DynamicTableResultsComponent } from './pages/resultados/dynamic-table-results/dynamic-table-results.component';
import { DynamicTableComponent } from './components/dynamic-table/dynamic-table.component';
import { JuradoComponent } from './pages/jurado/table-jurado/jurado.component';
import { UsersComponent } from './pages/users/users.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AdminComponent } from './pages/admin/admin.component';
import { DynamicTableAdminComponent } from './pages/admin/dynamic-table-admin/dynamic-table-admin.component';
import { MatIconModule } from '@angular/material/icon';
import { ToastrModule } from 'ngx-toastr';

@NgModule({
  declarations: [
    AppComponent,
    FormLoginComponent,
    HomeComponent,
    HeaderComponent,
    NotFoundComponent,
    TestComponent,
    ResultsMenuComponent,
    DynamicTableResultsComponent,
    DynamicTableComponent,
    JuradoComponent,
    UsersComponent,
    AdminComponent,
    DynamicTableAdminComponent,
  ],
  imports: [
    MatPaginatorModule,
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    MatCardModule,
    MatTableModule,
    MatSortModule,
    BrowserAnimationsModule,
    MatProgressSpinnerModule,
    NgChartsModule,
    MatIconModule,
    ToastrModule.forRoot(),
  ],
  exports: [MatCardModule, MatTableModule, MatSortModule],
  providers: [CookieService],
  bootstrap: [AppComponent],
})
export class AppModule {}
