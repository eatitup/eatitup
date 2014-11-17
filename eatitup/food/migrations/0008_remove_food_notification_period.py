# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20141116_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='notification_period',
        ),
    ]
