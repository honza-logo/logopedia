# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='dictionary_images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slovnik.Category')),
            ],
        ),
    ]