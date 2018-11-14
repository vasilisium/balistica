import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  svg = `<?xml version="1.0" encoding="utf-8"?>
  <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
     viewBox="0 0 250 250" style="enable-background:new 0 0 250 250;" xml:space="preserve">
  <style type="text/css">
    .st0{fill:#FFFFFF;}
    .st1{opacity:0.9;}
  </style>
  <g>
    <g>
      <polygon class="st0" points="125,153.4 100.3,153.4 88.6,182.6 88.6,182.6 66.9,182.6 66.8,182.6 125,52.1 125,52.2 125,52.2 
        125,30 125,30 31.9,63.2 46.1,186.3 125,230 125,230 125,153.4 		"/>
      <polygon class="st0" points="108,135.4 125,135.4 125,135.4 125,94.5 		"/>
    </g>
    <g class="st1">
      <polygon class="st0" points="125,153.4 149.7,153.4 161.4,182.6 161.4,182.6 183.1,182.6 183.2,182.6 125,52.1 125,52.2 125,52.2 
        125,30 125,30 218.1,63.2 203.9,186.3 125,230 125,230 125,153.4 		"/>
      <polygon class="st0" points="142,135.4 125,135.4 125,135.4 125,94.5 		"/>
    </g>
  </g>
  </svg>`

}
