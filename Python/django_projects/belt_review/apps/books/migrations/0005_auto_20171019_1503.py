# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('books', '0004_auto_20171019_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ManyToManyField(blank='True', related_name='books', to='users.User'),
        ),
    ]
