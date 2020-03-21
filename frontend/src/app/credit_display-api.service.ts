import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs';
import 'rxjs/add/operator/catch';
import {API_URL} from './env';
import {Credit} from './credit_display.model';

@Injectable()
export class CreditApiService {

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getCredits(): Observable<Credit[]> {
    return this.http
      .get(`${API_URL}/credits`)
      .catch(CreditApiService._handleError);
  }
}
