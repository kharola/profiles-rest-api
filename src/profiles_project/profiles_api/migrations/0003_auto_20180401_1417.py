# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-01 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20180401_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_stalf',
            new_name='is_staff',
        ),
    ]
