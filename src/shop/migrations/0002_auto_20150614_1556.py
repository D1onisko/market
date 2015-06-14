# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('price', 'title'), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='order',
            new_name='price',
        ),
    ]
