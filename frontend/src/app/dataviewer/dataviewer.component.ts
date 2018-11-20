import { Component, OnInit, Inject } from '@angular/core';
import { APIView, SootingView } from '../shared/balisticsa.model'
import { BalisticsAPIService } from '../shared/balistics-api.service';
// import { MatTableDataSource } from '@angular/material';
import { Observable } from 'rxjs';
import { DataSource } from '@angular/cdk/collections';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material';

import {DialogComponent} from './dialog/dialog.component'

@Component({
  selector: 'app-dataviewer',
  templateUrl: './dataviewer.component.html',
  styleUrls: ['./dataviewer.component.scss']
})

export class DataviewerComponent implements OnInit {
  dataSource = new ShootingsDS(this.service);

  constructor(
    private service:BalisticsAPIService, 
    public dialog: MatDialog
  ) {}

  ngOnInit() {}

  displayedColumns: ReadonlyArray<string> = [
    'owner', 
    'wepon',
    'date_Shooting', 
    'ammo', 
    'document', 
    'safe_number',
  ];

  clickRow(row) {
    const dialogRef = this.dialog.open(DialogComponent, {width: '400px', data: row});

    dialogRef.afterClosed().subscribe(result => {
      console.log('closed');

    });
    
  }
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


