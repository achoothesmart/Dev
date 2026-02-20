import { Component, AfterViewInit } from '@angular/core';
import { sayHello } from './utility';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements AfterViewInit {
  title = 'SampleApp';

  ngAfterViewInit(): void {
      // sayHello(this);
      
  }
}
