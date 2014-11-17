# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_unit_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='notification_period',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 23, 20, 59, 48, 316208)),
            preserve_default=True,
        ),
    ]
