# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20150614_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=None, verbose_name='Is present'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='is_recommend',
            field=models.BooleanField(default=None, verbose_name='Recomendation'),
            preserve_default=True,
        ),
    ]
