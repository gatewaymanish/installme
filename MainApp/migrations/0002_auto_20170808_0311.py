# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setuptemplate',
            name='step',
        ),
        migrations.AddField(
            model_name='steps',
            name='setup',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='MainApp.SetupTemplate'),
        ),
    ]