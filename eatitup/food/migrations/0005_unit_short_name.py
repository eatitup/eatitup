# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_unitconversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='short_name',
            field=models.CharField(default='g', max_length=5),
            preserve_default=False,
        ),
    ]
