import { Component, OnInit } from '@angular/core';
import {CategoryService} from '../category.service';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})
export class CategoriesComponent implements OnInit {
  categories;

  constructor(private service: CategoryService) { }

  ngOnInit(): void {
    this.getCategories();
  }
  getCategories() {
    const a = this.service.getCategory();
    a.subscribe(cat => this.categories = cat );
  }
}
