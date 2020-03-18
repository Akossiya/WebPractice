import { Injectable } from '@angular/core';
import {books} from './books';
import {Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BooksService {
  book = books;

  constructor() { }
  getBook(): Observable<any[]> {
    return of(this.book);
  }
}
