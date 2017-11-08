# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 16:41
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20171102_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userlanguage',
            options={'ordering': ('language',), 'verbose_name': 'language', 'verbose_name_plural': 'languages'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]