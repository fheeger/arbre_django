# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-01 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_auto_20180701_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/img', verbose_name='image'),
        ),
    ]
