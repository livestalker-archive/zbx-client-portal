# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20171106_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zabbix_user_id',
            field=models.IntegerField(default=0),
        ),
    ]
