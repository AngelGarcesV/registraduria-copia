import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CandidatosRoutingModule } from './candidatos-routing.module';
import { TableCandidatoComponent } from './table-candidato/candidato.component';

@NgModule({
  declarations: [TableCandidatoComponent],
  imports: [CommonModule, CandidatosRoutingModule],
})
export class CandidatosModule {}
