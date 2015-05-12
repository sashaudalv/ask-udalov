# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ask.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0013_auto_20150429_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(upload_to=ask.models.get_upload_filename),
        ),
    ]
