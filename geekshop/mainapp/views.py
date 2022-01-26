import json
import os
from django.shortcuts import render

links_menu = [
    {"href": "main", "name": "домой"},
    {"href": "products", "name": "продукты"},
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
    return render(
        request,
        "mainapp/index.html",
        context={"links_menu": links_menu, "catalog": catalog, "title": "магазин"},
    )


def products(request):
    with open("static/json/prod_menu.json", "r", encoding="utf-8") as f:
        prod_menu = json.load(f)
    return render(
        request,
        "mainapp/products.html",
        context={
            "links_menu": links_menu,
            "catalog": catalog,
            "title": "каталог",
            "prod_menu": prod_menu,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={"links_menu": links_menu, "title": "контакты"},
    )
