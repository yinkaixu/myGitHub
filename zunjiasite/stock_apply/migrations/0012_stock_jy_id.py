# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-17 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_apply', '0011_delete_zjjy_ipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='jy_id',
            field=models.IntegerField(default=0),
        ),
    ]
