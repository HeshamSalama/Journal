# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='close',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='stock',
            name='open',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.CharField(max_length=500),
        ),
    ]
