# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-11 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_apply', '0006_auto_20180108_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='stockname',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='stock',
            name='pin_yin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterModelTable(
            name='stock',
            table='ZJ_HK_IPO',
        ),
    ]
