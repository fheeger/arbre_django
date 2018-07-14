# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-25 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_individual_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='gender',
            field=models.CharField(choices=[('F', 'femme'), ('H', 'homme'), ('A', 'autre')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/img', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='occupation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='individual',
            name='place_of_birth',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_of_birth', to='menu.Location'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='place_of_death',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_of_death', to='menu.Location'),
        ),
        migrations.AlterField(
            model_name='individual',
            name='place_of_residence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='church',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='department',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='gedcom_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='place_of_marriage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_of_marriage', to='menu.Location'),
        ),
    ]