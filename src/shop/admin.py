# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.flatpages import admin as fp_admin, models as fp_models

from src.shop import models

class WysiwygAdmin(admin.ModelAdmin):

    class Meta:
        wysiwyg_fields = ()

    class Media:
        js = ('%stiny_mce/tiny_mce.js' % settings.STATIC_URL,
              '%sjs/wysiwyg.js' % settings.STATIC_URL,)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(WysiwygAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in self.Meta.wysiwyg_fields:
            field.widget.attrs['class'] = 'wysiwyg %s' % field.widget.attrs.get('class', '')
        return field

class WysiwygFlatPageAdmin(fp_admin.FlatPageAdmin, WysiwygAdmin):
    class Meta:
        wysiwyg_fields = ('content')

admin.site.unregister(fp_models.FlatPage)
admin.site.register(fp_models.FlatPage, WysiwygFlatPageAdmin)

class Category(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'parent', 'is_active', 'price',)
    fieldsets = ((None, {'fields': ('parent', 'title', 'slug', ('is_active', 'price'),)}), )
    search_fields = ('title',)
admin.site.register(models.Category, Category)