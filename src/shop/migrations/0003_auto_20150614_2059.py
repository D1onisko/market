# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150614_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('slug', models.SlugField(max_length=80)),
                ('color', models.CharField(default=b'#6699bb', help_text='HEX color, as #RRGGBB', max_length=7, verbose_name='Color')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('slug', models.SlugField(max_length=80)),
                ('price', models.FloatField(verbose_name='Price')),
                ('is_active', models.BooleanField(verbose_name='Is present')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='Recomendation')),
                ('desc', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('tech', models.TextField(null=True, verbose_name='Technical Info', blank=True)),
                ('image', models.ImageField(upload_to='itempics', verbose_name='Image')),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name='Tags', blank=True)),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
                ('base_url', models.CharField(max_length=255)),
                ('category', models.ForeignKey(verbose_name='Category', to='shop.Category')),
                ('color', models.ManyToManyField(to='shop.Color', verbose_name='Color', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
    ]
