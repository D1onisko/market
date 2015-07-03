# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin

from src.shop import models


class Product(admin.ModelAdmin):
    admin.site.disable_action('delete_selected')

    def full_delete_selected(request, self, obj,):
        for o in obj.all():
            o.delete()

    full_delete_selected.short_description = 'Удалить выбранные лоты'
    actions = ['full_delete_selected']
    list_display = ('title', 'price', 'slug', 'descp',
                    'category', 'get_mini_html',)
    fieldsets = ((None, {'fields': ('user_name', 'title', 'descp',
                                    'price', 'category', 'phone',
                                    'hide_phone', 'adress', 'image',)}), )
    search_fields = ('title', 'category')
admin.site.register(models.Product, Product)


class Category(admin.ModelAdmin):
    list_display = ('title', 'parent', 'is_active', )
    fieldsets = ( (None, {'fields': ('parent', 'title', ('is_active',),)}), )
    search_fields = ('title',)
admin.site.register(models.Category, Category)