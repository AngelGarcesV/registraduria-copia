import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import { CookieService } from 'ngx-cookie-service';
import { JuradoServiceService } from 'src/app/services/jurado-service.service';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort, Sort } from '@angular/material/sort';
import { MatPaginator } from '@angular/material/paginator';
import { LiveAnnouncer } from '@angular/cdk/a11y';

@Component({
  selector: 'app-table-candidato',
  templateUrl: './candidato.component.html',
  styleUrls: ['./candidato.component.scss'],
})
export class TableCandidatoComponent implements AfterViewInit, OnInit {
  activo = false;
  text: string = '';
  mesa: any = '';
  vote: number = 0;
  public loading: boolean = false;
  @ViewChild(MatSort) sort: MatSort = new MatSort();
  @ViewChild(MatPaginator)
  paginator!: MatPaginator;

  displayedColumns: any[] = ['name', 'partido', 'acciones'];
  dataSource = new MatTableDataSource();

  constructor(
    private getGateway: LoginService,
    private juradoService: JuradoServiceService,
    private cookieService: CookieService,
    private _liveAnnouncer: LiveAnnouncer
  ) {}

  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }
  ngOnInit(): void {
    this.juradoService.getDataCandidate().subscribe((res: any) => {
      const vote = {
        vote: 0,
      };
      res.forEach((element: any) => {
        element = Object.assign(element, vote);
      });
      this.dataSource = new MatTableDataSource(res);
      this.ngAfterViewInit();
    });
    this.getGateway
      .getTable(
        this.cookieService.get('userId'),
        this.cookieService.get('token')
      )
      .subscribe((res: any) => {
        this.text = `Mesa asignada : ${res.mesa}`;
        this.mesa = res.mesa;
      });
  }
  announceSortChange(sortState: Sort) {
    if (sortState.direction) {
      this._liveAnnouncer.announce(`Sorted ${sortState.direction}ending`);
    } else {
      this._liveAnnouncer.announce('Sorting cleared');
    }
  }

  printConsole(a: any, b: any) {
    console.log(a + ' ' + b);
  }
  sendVotes(a: any, b: any) {
    this.loading = true;
    const data = {
      candidateId: a,
      tableId: parseInt(this.mesa),
      vote: parseInt(b),
    };
    this.juradoService.createResult(data).subscribe((res: any) => {
      this.loading = false;
      this.juradoService.sendNotification();
    });
  }

  activateCandidate(id: any) {
    this.activo = !this.activo;
  }
}
