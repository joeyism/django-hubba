from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.forms.models import model_to_dict

from .models import Product, Buyer, Recommendation


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def product_details(request, name):
    product = get_object_or_404(Product, name=name)
    return render(request, "product_details.html", model_to_dict(product))

def buyer_details(request, owner):
    buyer = get_object_or_404(Buyer, owner=owner)
    recomm_list = get_list_or_404(Recommendation, buyer=buyer)
    return render(
        request,
        "buyer_details.html",
        dict(model_to_dict(buyer), **{"recommendations": recomm_list})
    )



