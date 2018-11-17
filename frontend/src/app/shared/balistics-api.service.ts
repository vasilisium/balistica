import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

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
    let result = this.httpClient.get(this.rootAPI_URL + '/shooting/')
    .pipe(map( data => { return data['results'] }))
    console.log(result);
    return result;
  }
}
