# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0003_auto_20150421_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeType', models.IntegerField(default=0)),
                ('answer', models.ForeignKey(to='ask.Answer')),
                ('user', models.ForeignKey(to='ask.User')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeType', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='like',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='like',
            name='question',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='tag',
            name='questions',
            field=models.ManyToManyField(to='ask.Question'),
        ),
        migrations.AddField(
            model_name='questionlike',
            name='question',
            field=models.ForeignKey(to='ask.Question'),
        ),
        migrations.AddField(
            model_name='questionlike',
            name='user',
            field=models.ForeignKey(to='ask.User'),
        ),
        migrations.AlterUniqueTogether(
            name='questionlike',
            unique_together=set([('user', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='answerlike',
            unique_together=set([('user', 'answer')]),
        ),
    ]
