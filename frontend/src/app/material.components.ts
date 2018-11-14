import { NgModule } from '@angular/core';

import {MatToolbarModule} from '@angular/material/toolbar'
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatTableModule} from '@angular/material/table';
// import {MatPaginator, MatTableDataSource, MatSort} from '@angular/material';


var modules = [
    MatToolbarModule, 
    MatIconModule, 
    MatButtonModule, 
    MatTableModule,
    // MatPaginator,
    // MatTableDataSource,
    // MatSort,
]

@NgModule ({
    imports : modules,
    exports : modules,
})

export class MaterialModule{}