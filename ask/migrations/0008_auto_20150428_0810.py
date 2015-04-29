# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0007_auto_20150421_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='ask.Tag'),
        ),
    ]
