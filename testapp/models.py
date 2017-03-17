# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text.encode('utf-8', errors='replace')


class Answer(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text.encode('utf-8', errors='replace')


class Task(models.Model):
    question = models.ForeignKey(Question, blank=True, null=True)
    options = models.ManyToManyField(Answer, blank=True, related_name='options')
    answers = models.ManyToManyField(Answer, blank=True, related_name='answers')

    def __str__(self):
        return self.question.text.encode('utf-8', errors='replace')


class Variant(models.Model):
    name = models.CharField(max_length=140, default='Вариант')
    questions = models.ManyToManyField(Question, blank=True, null=True)

    def __str__(self):
        return self.name
