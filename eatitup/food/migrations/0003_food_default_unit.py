# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='default_unit',
            field=models.ForeignKey(default=1, blank=True, to='food.Unit'),
            preserve_default=False,
        ),
    ]
