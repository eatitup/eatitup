# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('store_cupboard', '0003_item_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='use_by_date',
            field=models.DateTimeField(default=datetime.date(2014, 11, 16)),
            preserve_default=False,
        ),
    ]
