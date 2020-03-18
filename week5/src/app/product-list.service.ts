import { Injectable } from '@angular/core';
import {products} from './products';
import {Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductListService {
  product = products;

  constructor() { }
  getProduct(): Observable<any[]> {
     return of(this.product);
  }
}
