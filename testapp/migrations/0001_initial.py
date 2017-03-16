# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-14 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.ManyToManyField(blank=True, related_name='answers', to='testapp.Answer')),
                ('options', models.ManyToManyField(blank=True, related_name='options', to='testapp.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Question')),
            ],
        ),
    ]
