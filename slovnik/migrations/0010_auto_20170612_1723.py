# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 15:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slovnik', '0009_auto_20170612_1703'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestVariations',
            new_name='TestVariant',
        ),
    ]
