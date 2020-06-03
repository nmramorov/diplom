import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {Sheet} from '../../sheet';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class SheetService {

  private sheetsUrl = 'http://127.0.0.1:8000/participants_app/sheets_api';
  constructor(private http: HttpClient) { }

  getSheets(): Observable<Sheet[]> {
    return this.http.get<Sheet[]>(this.sheetsUrl);
  }

  getSheet(identifier: number): Observable<Sheet> {
      const url = `${this.sheetsUrl}/${identifier}`;
      return this.http.get<Sheet>(url).pipe(
        catchError(this.handleError<Sheet>(`getSheet id=${identifier}`))
      );
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }

}
