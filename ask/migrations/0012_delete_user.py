# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0011_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
