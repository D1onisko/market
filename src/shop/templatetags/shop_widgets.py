# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django import template


from src.shop import models

register = template.Library()

@register.inclusion_tag('shop/inclusion/categories_list.html')
def categories_list_tag():
    return {
        'categories': models.Category.objects.filter(is_active=True)
    }
