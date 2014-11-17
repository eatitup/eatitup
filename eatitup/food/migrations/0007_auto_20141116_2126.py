# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_food_notification_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='notification_period',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 23, 21, 26, 17, 221248), blank=True),
        ),
    ]
