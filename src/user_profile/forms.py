# coding=utf-8
from django import forms
from src.shop.models import Product
from django.contrib.contenttypes.models import ContentType


class AddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'title', 'descp', 'price', \
                 'image', 'category', 'phone', \
                 'hide_phone', 'adress',


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'descp', 'title', 'price', 'image'

