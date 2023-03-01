import { EventEmitter, Injectable, Output } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class EventListenerService {
  @Output() setLogged = new EventEmitter<any>();
  @Output() formLog = new EventEmitter<any>();

  constructor() { }
}
