# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-14 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20170507_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='picture_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
