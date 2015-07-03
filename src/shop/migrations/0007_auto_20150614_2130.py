# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20150614_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('phone', models.CharField(max_length=16, verbose_name='Phone')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='Registered')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.FloatField()),
                ('order', models.ForeignKey(to='shop.Order')),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=64, verbose_name='Title')),
                ('value', models.CharField(max_length=128, verbose_name='Value')),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
            options={
                'ordering': ('key',),
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
