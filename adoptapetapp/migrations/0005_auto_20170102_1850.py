# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptApetApp', '0004_auto_20170102_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='user_name',
            new_name='user',
        ),
    ]
