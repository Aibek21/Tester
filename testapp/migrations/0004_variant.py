# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-16 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('testapp', '0003_auto_20170315_0352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.ManyToManyField(to='testapp.Task')),
            ],
        ),
    ]
