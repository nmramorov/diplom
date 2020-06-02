import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {Sheet} from '../../sheet';

@Injectable({
  providedIn: 'root'
})
export class SheetService {

  private sheetsUrl = 'http://127.0.0.1:8000/participants_app/sheets_api/';
  constructor(private http: HttpClient) { }

  getSheets(): Observable<Sheet[]> {
    return this.http.get<Sheet[]>(this.sheetsUrl);
  }

}
