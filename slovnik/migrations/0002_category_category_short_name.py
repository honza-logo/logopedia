# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slovnik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_short_name',
            field=models.CharField(default='abc', max_length=25),
        ),
    ]
