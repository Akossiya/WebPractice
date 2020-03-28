from django.shortcuts import render

# Create your views here.
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Product
from api.models import Category
from django.http import Http404



def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        raise Http404
    return JsonResponse(product.to_json())

def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        raise Http404
    return JsonResponse(category.to_json())
def category_product(request, id):
    category = Category.objects.get(id=id)
    product = Product.objects.all()
    return JsonResponse(product.to_json())