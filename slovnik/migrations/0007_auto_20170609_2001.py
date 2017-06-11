# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slovnik', '0006_word_word_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='image',
            field=models.ImageField(upload_to='words_images'),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_short_name',
            field=models.CharField(max_length=25),
        ),
    ]
