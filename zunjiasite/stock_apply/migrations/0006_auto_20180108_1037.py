# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-08 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_apply', '0005_auto_20180103_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='pin_yin',
            field=models.CharField(max_length=10, null=True),
        ),
    ]