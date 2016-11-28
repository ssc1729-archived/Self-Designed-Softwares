# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 01:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('game_id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_description', models.CharField(max_length=256)),
                ('display_options', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='quiz_game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_lock', models.IntegerField(default=-1)),
                ('game_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastest_finger_first.game')),
                ('question_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastest_finger_first.question')),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_id', models.IntegerField()),
                ('questions_answered', models.IntegerField(default=0)),
                ('tame_taken', models.IntegerField(default=0)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastest_finger_first.game')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=1)),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
