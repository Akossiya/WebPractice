import { Component, OnInit } from '@angular/core';
import {BooksService} from '../books.service';

@Component({
  selector: 'app-books-list',
  templateUrl: './books-list.component.html',
  styleUrls: ['./books-list.component.css']
})
export class BooksListComponent implements OnInit {
  books;
  constructor(
    private service: BooksService) { }

  ngOnInit(): void {
    this.getBook();
  }
  getBook() {
    const a = this.service.getBook();
    a.subscribe(b => this.books = b );
  }

}
