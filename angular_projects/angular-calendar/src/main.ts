import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
// import { CalendarComponent } from './app/calendar/calendar.component';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
