import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-dynamic-table-admin',
  templateUrl: './dynamic-table-admin.component.html',
  styleUrls: ['./dynamic-table-admin.component.scss'],
})
export class DynamicTableAdminComponent implements OnInit {
  @Input() title: string = '';
  constructor(private route: ActivatedRoute) {}
  columnas: any[] = [{ titulo: 'default', name: 'default' }];
  displayedColumns: any[] = ['default'];
  ngOnInit(): void {
    this.elegirColumnas();
  }

  elegirColumnas() {
    this.columnas = [
      { titulo: 'Nombre completo', name: 'name' },
      { titulo: 'Correo', name: 'mail' },
    ];
    this.displayedColumns = ['name', 'mail'];

    // if (this.text == 'usuario') {
    //   // en cada tipo se determinan las columnas que se van a mostrar , que a su vez son el nombre
    //   // del parametro que se encuentra en el json que devuelve la API al consultarla
    // }
  }
}
