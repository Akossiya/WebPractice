import { Component, OnInit } from '@angular/core';
import {CategoryService} from '../category.service';

@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  styleUrls: ['./category-list.component.css']
})
export class CategoryListComponent implements OnInit {
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
