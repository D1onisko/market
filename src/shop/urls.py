# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('src.shop.views',


    url(r'^product/get/(?P<product_id>\d+)/', 'product_detail', name='product_detail'),
    url(r'^', 'index', name='index'),

)
