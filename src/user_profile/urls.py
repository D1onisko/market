# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('src.user_profile.views',

    url(r'^accounts/addform/', 'addform', name='addform'),
    url(r'^accounts/done/', 'done', name='done'),
    url(r'^accounts/profile/', 'profile', name='profile'),
    url(r'^profile/redaktor/get/(?P<lot_id>\d+)/', 'redaktor', name='redaktor'),

)
