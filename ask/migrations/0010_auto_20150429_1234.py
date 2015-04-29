# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0009_auto_20150429_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='ask.CustomUser'),
        ),
        migrations.AlterField(
            model_name='answerlike',
            name='user',
            field=models.ForeignKey(to='ask.CustomUser'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='ask.CustomUser'),
        ),
        migrations.AlterField(
            model_name='questionlike',
            name='user',
            field=models.ForeignKey(to='ask.CustomUser'),
        ),
    ]
