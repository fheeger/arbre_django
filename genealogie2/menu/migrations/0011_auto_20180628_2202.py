# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-28 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20180627_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
