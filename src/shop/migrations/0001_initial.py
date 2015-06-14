# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('slug', models.SlugField(max_length=80)),
                ('is_active', models.BooleanField(default=None, verbose_name='Is active')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('base_url', models.CharField(max_length=225)),
                ('parent', models.ForeignKey(verbose_name='Parent', blank=True, to='shop.Category', null=True)),
            ],
            options={
                'ordering': ('order', 'title'),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
    ]
