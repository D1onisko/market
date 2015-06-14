# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

from datetime import datetime

from sorl.thumbnail.shortcuts import get_thumbnail
from tagging.fields import TagField
from tagging.utils import parse_tag_input


class Category(models.Model):
    """
    Обозначение категории.
    """
    parent = models.ForeignKey(u'self', verbose_name=_(u'Parent'), blank=True, null=True)
    title = models.CharField(verbose_name=_(u'Title'), max_length=64)
    slug = models.SlugField(max_length=80)
    is_active = models.BooleanField(verbose_name=_(u'Is active'), default=None)
    price = models.IntegerField(verbose_name=_(u'Order'), default=0)
    base_url = models.CharField(max_length=225)

    class Meta:
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')
        ordering = ('price', 'title')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:category', args=[self.slug])

    def diff(self):
        has_diff = False
        changed_fields = {}
        old = self.__class__.objects.get(pk=self.pk)
        for field in ('title',):
            model_value = getattr(old, field)
            new_value = getattr(self, field)
            if model_value != new_value:
                has_diff = True
                changed_fields[field] = {
                    'old': model_value,
                    'new': new_value,
                }
        return has_diff, changed_fields

    def save(self, *args, **kwargs):
        """
        Если модель обновляется с теми же данными, то игнорировать это
        """
        out = []
        if self.pk:
            is_changed, changed_field = self.diff()
            out = changed_field
        super(Category, self).save(*args, **kwargs)
        return out

class Color(models.Model):
    """
    Описание цвета товара
    """
    title = models.CharField(verbose_name=_('Title'), max_length=64)
    slug = models.SlugField(max_length=80)
    color = models.CharField(verbose_name=_('Color'),max_length=7,
                             default='#6699bb', # без этого глючит farbtastic
                             help_text=_(u'HEX color, as #RRGGBB'))

    class Meta:
        verbose_name = _(u'Color')
        verbose_name_plural = _(u'Colors')
        ordering = ('title',)

    def __unicode__(self):
        return self.title



