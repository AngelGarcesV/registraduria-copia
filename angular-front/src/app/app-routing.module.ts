// Libs
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
// Páginas
import { HomeComponent } from './components/home/home.component';
import { TestComponent } from './pages/test/test.component';
import { UsersComponent } from './pages/users/users.component';
import { AdminComponent } from './pages/admin/admin.component';
const routes: Routes = [
  {
    path: 'seguridad',
    loadChildren: () =>
      import('./pages/seguridad/seguridad.module').then(
        (m) => m.SeguridadModule
      ),
  },
  {
    path: 'resultados',
    loadChildren: () =>
      import('./pages/resultados/resultados.module').then(
        (m) => m.ResultadosModule
      ),
  },
  {
    path: 'jurado',
    loadChildren: () =>
      import('./pages/jurado/jurado.module').then((m) => m.JuradoModule),
  },
  {
    path: 'candidatos',
    loadChildren: () =>
      import('./pages/candidatos/candidatos.module').then(
        (m) => m.CandidatosModule
      ),
  },
  {
    path: 'home',
    component: HomeComponent,
  },
  {
    path: '',
    component: HomeComponent,
  },
  {
    path: 'test',
    component: TestComponent,
  },

  {
    path: 'users',
    component: UsersComponent,
  },
  {
    path: 'admin',
    component: AdminComponent,
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
