import { formatDate } from '@angular/common';
import { Component, OnInit } from '@angular/core';

interface CalendarEvent {
  title: string;
  date: Date;
}

interface Day {
  date: Date;
  events: CalendarEvent[];
}

@Component({
  selector: 'app-calendar',
  templateUrl: './calendar.component.html',
  styleUrls: ['./calendar.component.css']
})
export class CalendarComponent implements OnInit {
  currentYear: number;
  currentMonth: number;
  days: Day[] = [];
  allEvents = [
    // { date: Date.now(), title: 'Today'},
    { date: new Date(2024, 7, 26), title: 'Birthday'},
    { date: new Date(2024, 7, 28), title: 'Baby shower'}
  ];

  constructor() {
    const today = new Date();
    this.currentYear = today.getFullYear();
    this.currentMonth = today.getMonth(); 
  }

  ngOnInit(): void {
    this.generateCalendar();
  }

  generateCalendar() {
    // Logic to generate days and events goes here
    this.days = [];
    const firstDay = new Date(this.currentYear, this.currentMonth, 1);
    const lastDay = new Date(this.currentYear, this.currentMonth + 1, 0);

    for (let day = firstDay; day <= lastDay; day.setDate(day.getDate() + 1)) {
      this.days.push({
        date: new Date(day),
        events: this.allEvents.filter(ev => 
          formatDate(day, 'dd/mm/yyyy', 'en-US') == formatDate(ev.date, 'dd/mm/yyyy', 'en-US')
        ) // Fetch events for the day
      });
    }
  }

  next() {
    if (this.currentMonth === 11) {
      this.currentMonth = 0;
      this.currentYear++;
    } else {
      this.currentMonth++;
    }
    this.generateCalendar();
  }

  prev() {
    if (this.currentMonth === 0) {
      this.currentMonth = 11;
      this.currentYear--;
    } else {
      this.currentMonth--;
    }
    this.generateCalendar();
  }
}
