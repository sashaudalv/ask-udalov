# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0012_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='user',
            new_name='user_ptr',
        ),
        migrations.RenameField(
            model_name='answerlike',
            old_name='user',
            new_name='user_ptr',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='user',
            new_name='user_ptr',
        ),
        migrations.RenameField(
            model_name='questionlike',
            old_name='user',
            new_name='user_ptr',
        ),
        migrations.AlterUniqueTogether(
            name='answerlike',
            unique_together=set([('user_ptr', 'answer')]),
        ),
        migrations.AlterUniqueTogether(
            name='questionlike',
            unique_together=set([('user_ptr', 'question')]),
        ),
    ]
