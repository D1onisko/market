# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20150614_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tech',
        ),
    ]
