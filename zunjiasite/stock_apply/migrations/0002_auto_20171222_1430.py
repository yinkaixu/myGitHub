# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_apply', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='date_begin',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='date_end',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='least_purchase',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='listing_date',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='open_amount',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='price_high',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='price_low',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='total_amount',
        ),
        migrations.AddField(
            model_name='stock',
            name='applystartdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='datetoaccount',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='exchange',
            field=models.CharField(default=b'HKEX', max_length=10),
        ),
        migrations.AddField(
            model_name='stock',
            name='issueenddate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='issuepriceceiling',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=8),
        ),
        migrations.AddField(
            model_name='stock',
            name='issuepricefloor',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=8),
        ),
        migrations.AddField(
            model_name='stock',
            name='issuetype',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='issuevolplanned',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=8),
        ),
        migrations.AddField(
            model_name='stock',
            name='proposedlistdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='publicnewshareplanned',
            field=models.DecimalField(null=True, max_digits=18, decimal_places=2),
        ),
        migrations.AddField(
            model_name='stock',
            name='tradeunit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='tradeunitpriceatceiling',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=4),
        ),
        migrations.AlterField(
            model_name='stock',
            name='code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stockname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
