# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_unit'),
        ('store_cupboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(default=1, to='food.Unit'),
            preserve_default=False,
        ),
    ]
