# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-17 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_apply', '0014_auto_20180117_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='jy_id',
        ),
    ]
