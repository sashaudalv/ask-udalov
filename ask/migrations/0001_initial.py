# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('isCorrect', models.BooleanField(default=False)),
                ('rating', models.IntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeType', models.CharField(max_length=10)),
                ('answer', models.ForeignKey(to='ask.Answers')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=200)),
                ('question_text', models.CharField(max_length=500)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('rating', models.IntegerField()),
                ('num_answers', models.IntegerField()),
                ('tags', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=15, unique=True)),
                ('nick_name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('avatar', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='ask.User'),
        ),
        migrations.AddField(
            model_name='likes',
            name='question',
            field=models.ForeignKey(to='ask.Question'),
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(to='ask.User'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(to='ask.Question'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(to='ask.User'),
        ),
    ]
