import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { User } from '../model/user';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiURL: string = 'http://localhost:3333';
  
  constructor(private http: HttpClient) { }

  createSession(user: User): Observable<any>{
    return this.http.post(`${this.apiURL}/sessions`, user)
  }

  createUser(user: User): Observable<any>{
    return this.http.post<User>(`${this.apiURL}/users`, user)
  }

}
