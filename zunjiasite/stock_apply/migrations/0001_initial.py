# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stockname', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=10)),
                ('price_low', models.CharField(max_length=20)),
                ('price_high', models.CharField(max_length=20)),
                ('total_amount', models.CharField(max_length=20)),
                ('open_amount', models.CharField(max_length=20)),
                ('least_purchase', models.CharField(max_length=20)),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField()),
                ('listing_date', models.DateField()),
                ('updatetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
