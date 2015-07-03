# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20150614_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_recommend',
            field=models.BooleanField(default=False, verbose_name='Recomendation'),
            preserve_default=True,
        ),
    ]
