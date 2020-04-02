import { Component, OnInit } from '@angular/core';
import { products } from '../products';
import { ActivatedRoute } from '@angular/router';
import {categories} from '../categories';
import {ProductListService} from '../product-list.service';


@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  products = products;
  category;
  constructor(
    private route: ActivatedRoute, private service: ProductListService
  ) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.category = categories[+params.get('categoryId')];
    });
    this.getProduct();
  }
  getProduct() {
    const a = this.service.getProduct();
    a.subscribe(cat => this.products = cat );
  }
}
