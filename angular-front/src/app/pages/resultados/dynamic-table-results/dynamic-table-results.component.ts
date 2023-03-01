import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-dynamic-table-results',
  templateUrl: './dynamic-table-results.component.html',
  styleUrls: ['./dynamic-table-results.component.scss'],
})
export class DynamicTableResultsComponent implements OnInit {
  constructor(private route: ActivatedRoute) {}
  text: string = '';
  columnas: any[] = [{ titulo: 'default', name: 'default' }];
  displayedColumns: any[] = ['default'];

  ngOnInit(): void {
    this.elegirColumnas(); // <--- Aquí se llama la funcion para que se ejecute al inicio
  }

  elegirColumnas() {
    this.route.queryParams.subscribe((params) => {
      // <--- Aquí se obtienen los parametros QUERY de la url
      this.text = this.capitalizarPrimeraLetra(params['type']);
      // <--- Aquí se obtiene el valor del parametro QUERY 'type' que se menciono en el html con nombre 'type'
    });
    if (this.text.toLowerCase() == 'candidato') {
      this.columnas = [
        { titulo: 'Candidato', name: 'name' },
        { titulo: 'Partido', name: 'partido' },
        { titulo: 'Total de votos', name: 'totalVotes' },
      ];
      this.displayedColumns = ['name', 'partido', 'totalVotes'];
      // en cada tipo se determinan las columnas que se van a mostrar , que a su vez son el nombre
      // del parametro que se encuentra en el json que devuelve la API al consultarla
    } else if (this.text.toLowerCase() == 'mesas') {
      this.columnas = [
        { titulo: 'Mesa', name: 'id' },
        { titulo: 'Total de votos', name: 'votos' },
      ];
      this.displayedColumns = ['id', 'votos'];
    } else if (this.text.toLowerCase() == 'partido') {
      this.columnas = [
        { titulo: 'Partido', name: 'partido' },
        { titulo: 'Total de votos', name: 'votos' },
      ];
      this.displayedColumns = ['partido', 'votos'];
    }
  }

  capitalizarPrimeraLetra(str : string) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }
}
