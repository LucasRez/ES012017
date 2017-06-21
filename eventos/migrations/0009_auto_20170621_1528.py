# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-21 15:28
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0008_festa_nomefesta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bar',
            old_name='precoLitrao',
            new_name='media_cerveja',
        ),
        migrations.RemoveField(
            model_name='festa',
            name='nomeFesta',
        ),
        migrations.AddField(
            model_name='bar',
            name='bairro',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='bar',
            name='dias_aberto',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='bar',
            name='endereco',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='bar',
            name='horario',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='bar',
            name='mais_info',
            field=models.CharField(default='', help_text='Link para site/facebook/instagram/outros', max_length=100),
        ),
        migrations.AddField(
            model_name='bar',
            name='media_drinks',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bar',
            name='media_petiscos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bar',
            name='media_shots',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='esporte',
            name='bairro',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='esporte',
            name='dia',
            field=models.CharField(default='', help_text='DD/MM/AAAA', max_length=10),
        ),
        migrations.AddField(
            model_name='esporte',
            name='endereco',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='esporte',
            name='horario',
            field=models.CharField(default='', help_text='HH:MM', max_length=20),
        ),
        migrations.AddField(
            model_name='esporte',
            name='ingressos',
            field=models.CharField(default='', help_text='Masc/Fem/Unissex', max_length=50),
        ),
        migrations.AddField(
            model_name='esporte',
            name='jogos',
            field=models.CharField(default='', help_text='Insira os times participantes', max_length=100),
        ),
        migrations.AddField(
            model_name='esporte',
            name='mais_info',
            field=models.CharField(default='', help_text='Link para site/facebook/instagram/outros', max_length=100),
        ),
        migrations.AddField(
            model_name='esporte',
            name='modalidade',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='festa',
            name='atracoes',
            field=models.TextField(default=0, help_text='Escreva as atracoes com seus horarios'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='festa',
            name='bairro',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='festa',
            name='classEtaria',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='festa',
            name='dia',
            field=models.CharField(default='', help_text='DD/MM/AAAA', max_length=10),
        ),
        migrations.AddField(
            model_name='festa',
            name='endereco',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='festa',
            name='horario',
            field=models.CharField(default='', help_text='HH:MM', max_length=20),
        ),
        migrations.AddField(
            model_name='festa',
            name='ingressos',
            field=models.CharField(default='', help_text='Masc/Fem/Unissex', max_length=50),
        ),
        migrations.AddField(
            model_name='festa',
            name='mais_info',
            field=models.CharField(default='', help_text='Link para site/facebook/instagram/outros', max_length=100),
        ),
        migrations.AddField(
            model_name='teatro',
            name='bairro',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='teatro',
            name='dia',
            field=models.CharField(default='', help_text='DD/MM/AAAA', max_length=10),
        ),
        migrations.AddField(
            model_name='teatro',
            name='direcao',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='teatro',
            name='endereco',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='teatro',
            name='horario',
            field=models.CharField(default='', help_text='HH:MM', max_length=20),
        ),
        migrations.AddField(
            model_name='teatro',
            name='ingressos',
            field=models.CharField(default='', help_text='Masc/Fem/Unissex', max_length=50),
        ),
        migrations.AddField(
            model_name='teatro',
            name='mais_info',
            field=models.CharField(default='', help_text='Link para site/facebook/instagram/outros', max_length=100),
        ),
        migrations.AddField(
            model_name='teatro',
            name='producao',
            field=models.CharField(default='', max_length=20),
        ),
    ]