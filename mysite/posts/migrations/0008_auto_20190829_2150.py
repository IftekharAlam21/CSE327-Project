# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-29 15:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_auto_20190829_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='group',
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('user', 'message')]),
        ),
    ]
