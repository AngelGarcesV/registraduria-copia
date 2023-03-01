import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TableCandidatoComponent } from './table-candidato/candidato.component';

const routes: Routes = [
  {
    path: '',
    component: TableCandidatoComponent,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class CandidatosRoutingModule {}
