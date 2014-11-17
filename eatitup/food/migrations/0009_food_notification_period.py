# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_remove_food_notification_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='notification_period',
            field=models.IntegerField(default=7),
            preserve_default=True,
        ),
    ]
