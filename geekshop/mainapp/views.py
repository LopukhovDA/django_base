import json
import os
from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView


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


def main(request):
    products = Product.objects.all()[:3]
    return render(
        request,
        "mainapp/index.html",
        context={"links_menu": links_menu,
                 "catalog": products, "title": "магазин"},
    )


def get_hot_product():
    products = Product.objects.filter(is_active=True)

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(
        pk=hot_product.pk
    )[:3]

    return same_products


def products(request, pk=None, page=1):

    prod_menu = ProductCategory.objects.filter(is_active=True)

    if pk is not None:
        if pk == 0:
            category = {"pk": 0, "name": "все"}
            products = Product.objects.filter(
                is_active=True, category__is_active=True
            ).order_by("price")

        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(
                category__pk=pk, is_active=True, category__is_active=True
            ).order_by("price")

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        return render(
            request,
            "mainapp/products_list.html",
            context={
                "title": "каталог",
                "links_menu": links_menu,
                "category": category,
                "products": products_paginator,
                "prod_menu": prod_menu,
            },
        )

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    return render(
        request,
        "mainapp/products.html",
        context={
            "links_menu": links_menu,
            "catalog": same_products,
            "title": "каталог",
            "prod_menu": prod_menu,
            "hot_product": hot_product,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={"links_menu": links_menu, "title": "контакты"},
    )


class ProductView(DetailView):
    model = Product
    template_name = "mainapp/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "продукты"
        context["links_menu"] = links_menu
        context['prod_menu'] = ProductCategory.objects.filter(is_active=True)
        return context
