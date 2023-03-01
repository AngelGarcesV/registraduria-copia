import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { JuradoComponent } from './table-jurado/jurado.component';

const routes: Routes = [
  {
    path: '',
    component: JuradoComponent,
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class JuradoRoutingModule {}
