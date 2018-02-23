# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_apply', '0003_auto_20171222_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
