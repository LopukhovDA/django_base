import json
import os
from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket

links_menu = [
    {"href": "main", "name": "домой"},
    {"href": "products:index", "name": "продукты"},
    {"href": "contact", "name": "контакты"},
    {"href": "basket:view", "name": "корзина"},
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
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        prod_count = 0
        for prod in basket:
            prod_count += prod.quantity

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by("price")
            category = {"name": "все"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by("price")
        return render(
            request,
            "mainapp/products_list.html",
            context={
                "title": "каталог",
                "links_menu": links_menu,
                "category": category,
                "products": products,
                "prod_menu": prod_menu,
                "basket": basket,
                "count": prod_count,
            },
        )

    same_products = Product.objects.all()[2:5]

    return render(
        request,
        "mainapp/products.html",
        context={
            "links_menu": links_menu,
            "catalog": same_products,
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
