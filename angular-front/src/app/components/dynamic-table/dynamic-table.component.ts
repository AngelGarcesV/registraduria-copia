import {
  Component,
  OnInit,
  Input,
  ViewChild,
  AfterViewInit,
} from '@angular/core';
import { LiveAnnouncer } from '@angular/cdk/a11y';
import { ListarResultadosPublicosService } from 'src/app/services/listar-resultados-publicos.service';
import { MatSort, Sort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';

import { ChartData, ChartEvent, ChartType } from 'chart.js';

@Component({
  selector: 'app-dynamic-table',
  templateUrl: './dynamic-table.component.html',
  styleUrls: ['./dynamic-table.component.scss'],
})
export class DynamicTableComponent implements AfterViewInit, OnInit {
  public loading: boolean = true; // Aqui se establece la variable de loading para que se muestre el spinner

  // Doughnut
  public doughnutChartLabels: string[] = [];
  setearGrafica(data: any) {
    this.doughnutChartData = {
      labels: this.doughnutChartLabels,
      datasets: [{ data: data }],
    };
  }
  public doughnutChartData: ChartData<'doughnut'> = {
    labels: this.doughnutChartLabels,
    datasets: [{ data: [1, 1, 1, 1] }],
  };
  public doughnutChartType: ChartType = 'doughnut';

  @Input() text: string = '';
  @Input() columnas: any[] = [{ titulo: 'default', name: 'default' }];
  @Input() displayedColumns: any[] = ['default'];
  dataSource = new MatTableDataSource(); // <--- Aquí se crea el dataSource

  // <--- Aquí en el constructor se inyecta el servicio que se
  // creo en services/listar-resultados-publicos.service.ts
  constructor(
    private ResultadosServices: ListarResultadosPublicosService,
    private _liveAnnouncer: LiveAnnouncer
  ) {}

  @ViewChild(MatSort) sort: MatSort = new MatSort();
  @ViewChild(MatPaginator)
  paginator!: MatPaginator;

  ngOnInit() {
    // <--- Aquí se llama el objeto contruido anteriormente
    // para que se ejecute al inicio y se obtengan los datos de la API
    this.obtenerDatos();
  }

  isChart() {
    //Esta funcion es para reemplazar en el html el componente de tabla, por un grafico
    return this.text.toLowerCase() === 'congreso';
  }

  ngAfterViewInit() {
    // esta funcion le otorga la capacidad a la tabla de ordenarse SEGUN
    // los datos que se obtienen de la API
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }
  obtenerDatos() {
    if ('congreso' == this.text.toLowerCase()) {
      this.ResultadosServices.getResultados(this.text.toLowerCase()).subscribe((res: any) => {
        this.doughnutChartLabels = res.map((item: any) => item.partido);
        let percentajes = res.map((item: any) => item.porcentaje);
        this.setearGrafica(percentajes);
        this.loading = false;
      });
    } else {
      this.ResultadosServices.getResultados(this.text.toLowerCase()).subscribe((res: any) => {
        this.dataSource = new MatTableDataSource(res); // <--- Aquí se asigna el resultado de la API al dataSource
        this.ngAfterViewInit();
        this.loading = false; // <--- Aquí se desactiva el spinner cuando ya se obtienen los datos
        // <--- Aquí se llama la función que se creo en el ngAfterViewInit
        // para poder que se ejecute JUNTO con la API y se pueda ordenar la tabla
      });
    }
  }

  announceSortChange(sortState: Sort) {
    if (sortState.direction) {
      this._liveAnnouncer.announce(`Sorted ${sortState.direction}ending`);
    } else {
      this._liveAnnouncer.announce('Sorting cleared');
    }
  }
}
