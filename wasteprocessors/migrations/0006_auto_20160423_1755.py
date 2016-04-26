# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasteprocessors', '0005_auto_20160422_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='wasteprocessor',
            name='accepts_salvage',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='accepts_scrap',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='accepts_surplus',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='wasteprocessor',
            name='paid_service',
            field=models.BooleanField(default=False),
        ),
    ]
