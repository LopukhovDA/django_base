import json
import os
from django.shortcuts import render
from .models import ProductCategory, Product

links_menu = [
    {"href": "main", "name": "домой"},
    {"href": "products:index", "name": "продукты"},
    {"href": "contact", "name": "контакты"},
]

catalog = [
    {
        "name": "Прекрасный стул",
        "description": "Прекрасный выбор!",
        "img": "img/product-1.jpg",
    },
    {
        "name": "Удобные стулья",
        "description": "Замечательное удобство!",
        "img": "img/product-2.jpg",
    },
    {
        "name": "Стул повышенного качества",
        "description": "Не оторваться",
        "img": "img/product-3.jpg",
    },
]


# Create your views here.
def main(request):
    products = Product.objects.all()[:3]
    return render(
        request,
        "mainapp/index.html",
        context={"links_menu": links_menu, "catalog": products, "title": "магазин"},
    )


def products(request, pk=None):
    # with open("static/json/prod_menu.json", "r", encoding="utf-8") as f:
    #    prod_menu = json.load(f)
    prod_menu = ProductCategory.objects.all()
    products = Product.objects.all()

    return render(
        request,
        "mainapp/products.html",
        context={
            "links_menu": links_menu,
            "catalog": products,
            "title": "каталог",
            "prod_menu": prod_menu,
            "pk": pk,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={"links_menu": links_menu, "title": "контакты"},
    )
