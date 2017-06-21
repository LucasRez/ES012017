# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-21 15:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0009_auto_20170621_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='media_cerveja',
            field=models.DecimalField(decimal_places=2, default='00,00', max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]