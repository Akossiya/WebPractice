import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { products } from '../products';


@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  product;
  constructor(
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
      this.route.paramMap.subscribe(params => {
        this.product = products[+params.get('productId')];
      });
  }

}
