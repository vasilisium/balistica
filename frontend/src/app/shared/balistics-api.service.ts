import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

import { SootingView } from './balisticsa.model';

@Injectable({
  providedIn: 'root'
})
export class BalisticsAPIService {
  shootingRecord: SootingView;
  shootingData: SootingView[];
  private readonly rootAPI_URL:string = 'http://127.0.0.1:8000/api/v1';

  constructor(private httpClient:HttpClient) { }

  getShootings(): Observable<SootingView[]>{
    return this.httpClient.get<SootingView[]>(this.rootAPI_URL + '/shooting/');
  }
}
