import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss'],
})
export class AdminComponent implements OnInit {
  title: string = '';
  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe((params) => {
      // <--- Aquí se obtienen los parametros QUERY de la url
      this.title = params['title'];
      // <--- Aquí se obtiene el valor del parametro QUERY 'title' que se menciono en el html con nombre 'title'
    });
  }
}
