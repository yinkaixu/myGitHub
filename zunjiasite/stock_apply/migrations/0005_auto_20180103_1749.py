# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_apply', '0004_auto_20171229_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='issueprice',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=8),
        ),
        migrations.AddField(
            model_name='stock',
            name='marketcode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='pin_yin',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
