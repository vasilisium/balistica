import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';
import { MaterialModule } from './material.components';
import { HttpClientModule } from '@angular/common/http'

import { BalisticsAPIService } from './shared/balistics-api.service';

import { AppComponent } from './app.component';
import { NavComponent } from './nav/nav.component';
import { DataviewerComponent } from './dataviewer/dataviewer.component';
import {MatTableModule} from '@angular/material/table';


@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    DataviewerComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    HttpClientModule,
    MatTableModule,
  ],
  providers: [BalisticsAPIService],
  bootstrap: [AppComponent]
})
export class AppModule { }
