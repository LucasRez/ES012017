# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-16 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipoDoEvento', models.CharField(choices=[('BA', 'Bar'), ('ES', 'Esporte'), ('FE', 'Festa'), ('TE', 'Teatro')], max_length=2)),
                ('precoLitrao', models.FloatField(default=0.0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
