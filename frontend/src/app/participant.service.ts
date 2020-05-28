import { Injectable } from '@angular/core';
import { Participant} from '../../participant';
import {Observable, of} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {catchError, map, retry, tap} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ParticipantService {

  private participantsUrl = 'http://127.0.0.1:8000/participants_app/participants_api/';
  constructor(
    private http: HttpClient
  ) { }

  getParticipants(): Observable<Participant[]> {
    return this.http.get<Participant[]>(this.participantsUrl);
  }

  getParticipant(id: number): Observable<Participant> {
      const url = `${this.participantsUrl}/${id}`;
      return this.http.get<Participant>(url).pipe(
        catchError(this.handleError<Participant>(`getHero id=${id}`))
      );
  }

  private handleError<T>(operation = 'operation', result?: T) {
  return (error: any): Observable<T> => {

    // TODO: send the error to remote logging infrastructure
    console.error(error); // log to console instead
    // Let the app keep running by returning an empty result.
    return of(result as T);
  };
}
}
