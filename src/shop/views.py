# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from annoying.decorators import render_to

from src.shop.models import Product, Category


@render_to('shop/index.html')
def index(request):
    product_list = Product.objects.filter(hide_phone=True)
    return {'product_list': product_list}


# вывод детального описания лота
@render_to('shop/detail.html')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return {'product': product}

@render_to('shop/category.html')
def category(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    category_vivod = Product.objects.filter(category_id=pk)
    return {'category': obj, 'category_vivod': category_vivod}

