# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adoptApetApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('variety', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('weight', models.CharField(max_length=50)),
                ('photo', models.FileField(upload_to='')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoptApetApp.Person')),
            ],
        ),
    ]
