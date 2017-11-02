# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 14:21
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    UserLanguage = apps.get_model("userprofile", "UserLanguage")
    db_alias = schema_editor.connection.alias
    UserLanguage.objects.using(db_alias).bulk_create([
        UserLanguage(language="English", language_code="en"),
        UserLanguage(language="Russian", language_code="ru"),
    ])


def reverse_func(apps, schema_editor):
    UserLanguage = apps.get_model("userprofile", "UserLanguage")
    db_alias = schema_editor.connection.alias
    UserLanguage.objects.using(db_alias).filter(language="English", language_code="en").delete()
    UserLanguage.objects.using(db_alias).filter(language="Russian", language_code="ru").delete()


class Migration(migrations.Migration):
    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
