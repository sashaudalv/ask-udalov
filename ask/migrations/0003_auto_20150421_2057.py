# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0002_auto_20150421_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('isCorrect', models.BooleanField(default=False)),
                ('rating', models.IntegerField(default=0)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('question', models.ForeignKey(to='ask.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeType', models.CharField(max_length=10)),
                ('answer', models.ForeignKey(to='ask.Answer')),
                ('question', models.ForeignKey(to='ask.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='answers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='question',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to='ask.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='ask.User'),
        ),
    ]
