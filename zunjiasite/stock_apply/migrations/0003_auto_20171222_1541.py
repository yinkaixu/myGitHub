# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_apply', '0002_auto_20171222_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='issuevolplanned',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=2),
        ),
    ]
