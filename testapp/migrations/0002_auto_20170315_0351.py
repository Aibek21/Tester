# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-15 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='question',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.Question'),
        ),
    ]
