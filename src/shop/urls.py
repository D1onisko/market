# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('src.shop.views',

    url(r'^$', 'index', name='index'),
    url(r'^product/(?P<slug>[-\w]+)/$', 'product_detail', name='product_detail'),


)
