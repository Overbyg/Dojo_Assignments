# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin_level',
            field=models.IntegerField(default=0),
        ),
    ]
