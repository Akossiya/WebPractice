from django.urls import path
from api.views import product_list
from api.views import product_detail

urlpatterns = [
    path('products/', product_list),
    path('products/<int:id>', product_detail),
]