# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapi', '0002_auto_20170922_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='close',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='open',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='ticker',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='volume',
        ),
        migrations.AddField(
            model_name='stock',
            name='news',
            field=models.CharField(default='SOME STRING', max_length=1000),
        ),
    ]
