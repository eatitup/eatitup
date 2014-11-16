# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_food_default_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitConversion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('conversion', models.FloatField()),
                ('unit_a', models.ForeignKey(related_name=b'unit a', to='food.Unit')),
                ('unit_b', models.ForeignKey(related_name=b'unit b', to='food.Unit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
