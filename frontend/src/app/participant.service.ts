import { Injectable } from '@angular/core';
import { Participant} from '../../participant';
import { PARTICIPANTS} from './mock-participants';
import {Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ParticipantService {

  constructor() { }

  getParticipants(): Observable<Participant[]> {
    return of(PARTICIPANTS);
  }
}
