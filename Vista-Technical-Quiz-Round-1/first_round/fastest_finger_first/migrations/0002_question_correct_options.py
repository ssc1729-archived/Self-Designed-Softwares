# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastest_finger_first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_options',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
