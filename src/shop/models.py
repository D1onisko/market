# -*- coding: utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from PIL import Image
from sorl.thumbnail import ImageField
from autoslug import AutoSlugField
from autoslug.settings import slugify as default_slugify


def _add_mini(s):
    parts = s.split(".")
    parts.insert(-1, "mini")
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


def _del_mini(p):
    mini_path = _add_mini(p)
    if os.path.exists(mini_path):
        os.remove(mini_path)


def custom_slugify(value):
    """
    Функция для перевода русского текста  в поле Slug  модели Product
    """
    return default_slugify(value).replace('-', '_')


class Category(models.Model):
    """
    Описание категории
    """
    parent = models.ForeignKey(u'self', verbose_name=_(u'Parent'), blank=True, null=True, related_name=u'categories')
    title = models.CharField(verbose_name=_(u'Title'), max_length=64)
    slug = AutoSlugField(populate_from='title', slugify=custom_slugify)
    is_active = models.BooleanField(verbose_name=_(u'Is active'), default=None)

    class Meta:
        verbose_name = _(u'Category')
        verbose_name_plural = _(u'Categories')
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'category', [self.pk]


class Product(models.Model):
    """
    Определение продукта.
    """
    category = models.ForeignKey(Category, verbose_name=_(u'Category'), related_name=u'entries')
    user_name = models.ForeignKey(User, related_name='+', to_field=u'username')
    title = models.CharField(verbose_name=_(u'Title'), max_length=64)
    price = models.FloatField(verbose_name=_(u'Price'))
    phone = models.IntegerField(verbose_name=_(u'Phone'), max_length=16)
    hide_phone = models.BooleanField(verbose_name=_(u'Hide Phone'), default=None)
    adress = models.CharField(verbose_name=_(u'Address'), max_length=255, default=None)
    descp = models.TextField(verbose_name=_(u'Description'), null=True, blank=True)
    image = models.ImageField(verbose_name=_(u'Image'), upload_to=u'itempics')
    registered = models.DateTimeField(verbose_name=_(u'Registered'), auto_now_add=True)
    slug = AutoSlugField(populate_from='title', slugify=custom_slugify)

    class Meta:
        verbose_name = _(u'Product')
        verbose_name_plural = _(u'Products')
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def _get_mini_path(self):
        return _add_mini(self.image.path)

    mini_path = property(_get_mini_path)

    def get_mini_html(self):
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.image.url, _add_mini(self.image.url), self.descp)

    mini_html = property(get_mini_html)
    get_mini_html.short_description = 'Миниатюра'
    get_mini_html.allow_tags = True

    def save(self, force_insert=False, force_update=False, using=None):
        try:
            obj = Product.objects.get(id=self.id)
            if obj.image.path != self.image.path:
                _del_mini(obj.image.path)
                obj.image.delete()
        except:
            pass
        super(Product, self).save()
        img = Image.open(self.image.path)
        img.thumbnail(
            (128, 128),
            Image.ANTIALIAS
        )
        img.save(self.mini_path, 'JPEG')

    def delete(self, using=None):
        try:
            obj = Product.objects.get(id=self.id)
            _del_mini(obj.image.path)
            obj.image.delete()
        except (Product.DoesNotExist, ValueError):
            pass
        super(Product, self).delete()

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.pk)])
