# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('slovnik', '0013_auto_20170626_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testfourimagesitem',
            name='word_correct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='word_correct', to='slovnik.Word'),
        ),
    ]