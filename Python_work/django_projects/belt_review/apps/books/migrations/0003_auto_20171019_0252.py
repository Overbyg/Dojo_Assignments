# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-19 02:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20171018_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rating',
            new_name='number',
        ),
    ]