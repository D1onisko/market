# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin

from src.shop import models


class Product(admin.ModelAdmin):
    admin.site.disable_action('delete_selected')

    def full_delete_selected(self, request, obj,):
        for o in obj.all():
            o.delete()

    full_delete_selected.short_description = 'Удалить выбранные фото'
    actions = ['full_delete_selected']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'price', 'descp', 'category', 'get_mini_html',)
    fieldsets = ((None, {'fields': ('user_name', 'title', 'descp', 'slug', 'price', 'category','phone','hide_phone','adress', 'image',)}), )
    search_fields = ('title', 'category')
admin.site.register(models.Product, Product)


class Category(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'parent', 'is_active', )
    fieldsets = ( (None, {'fields': ('parent', 'title', 'slug', ('is_active',),)}), )
    search_fields = ('title',)
admin.site.register(models.Category, Category)