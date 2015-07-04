# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from annoying.decorators import render_to

from src.shop.models import Product


@render_to('shop/index.html')
def index(request):
    product_list = Product.objects.filter(hide_phone=True)
    return {'product_list': product_list}


# вывод детального описания лота
@render_to('shop/product.html')
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return {'product': product}
