# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-21 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_auto_20170317_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='isAnswer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='variant',
            name='tasks',
            field=models.ManyToManyField(blank=True, to='testapp.Task'),
        ),
    ]
