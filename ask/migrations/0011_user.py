# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0010_auto_20150429_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, unique=True)),
                ('nick_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('avatar', models.CharField(max_length=50)),
                ('isActive', models.BooleanField(default=True)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]
