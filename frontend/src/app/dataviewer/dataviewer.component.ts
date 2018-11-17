import { Component, OnInit } from '@angular/core';
import { APIView, SootingView } from '../shared/balisticsa.model'
import { BalisticsAPIService } from '../shared/balistics-api.service';
// import { MatTableDataSource } from '@angular/material';
import { Observable } from 'rxjs';
import { DataSource } from '@angular/cdk/collections';


// const ELEMENT_DATA: SootingView[] = [
//   {owner: 'o123', wepon: 'w123', date_Shooting: "new Date()", ammo: 'a123', document: 'd123', safe_number: 's123'},
//   {owner: 'o123', wepon: 'w123', date_Shooting: "new Date()", ammo: 'a123', document: 'd123', safe_number: 's123'},
// ]

@Component({
  selector: 'app-dataviewer',
  templateUrl: './dataviewer.component.html',
  styleUrls: ['./dataviewer.component.scss']
})

export class DataviewerComponent implements OnInit {
  
  dataSource = new ShootingsDS(this.service);

  constructor(private service:BalisticsAPIService) {}

  ngOnInit() {
    // this.service.getShootings();
  }

  displayedColumns: ReadonlyArray<string> = [
    'owner',
    'wepon', 
    'date_Shooting', 
    'ammo', 
    'document', 
    'safe_number',
  ];
}

export class ShootingsDS extends DataSource<any>{
  constructor (private service:BalisticsAPIService){
    super();
  }

  connect(): Observable<SootingView[]>{
    return this.service.getShootings();
  }

  disconnect(){}
}