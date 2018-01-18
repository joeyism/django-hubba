from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def product_details(request, name):
    product = get_object_or_404(Product, name=name)
    return HttpResponse("Product Page")





