# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20150614_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_recommend',
            field=models.BooleanField(default=None, verbose_name='Recomendation'),
            preserve_default=True,
        ),
    ]
