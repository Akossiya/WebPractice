from django.urls import path
from api.views import product_list
from api.views import product_detail
from api.views import category_list
from api.views import category_detail
from api.views import category_product

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>', product_detail),
    path('categories/', category_list),
    path('categories/<int:id>', category_detail()),
    path('categories/<int:id>/products/',category_product)
]