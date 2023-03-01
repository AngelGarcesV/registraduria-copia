import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DynamicTableResultsComponent } from './dynamic-table-results/dynamic-table-results.component';
import { ResultsMenuComponent } from './results-menu/results-menu.component';

const routes: Routes = [
  {
    path: '',
    component: ResultsMenuComponent
  },
  {
    path : ':id',
    component : DynamicTableResultsComponent
  }

];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ResultadosRoutingModule { }
