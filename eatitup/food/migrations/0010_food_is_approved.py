# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_food_notification_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='is_approved',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
