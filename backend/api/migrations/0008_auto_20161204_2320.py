# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-04 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20161204_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stops',
            name='stop_latitude',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stops',
            name='stop_longitude',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='tour',
            name='latitude',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='tour',
            name='longitude',
            field=models.CharField(max_length=25),
        ),
    ]