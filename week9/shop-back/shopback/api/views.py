from django.shortcuts import render

# Create your views here.
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from api.models import Product
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