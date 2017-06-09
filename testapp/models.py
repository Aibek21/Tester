# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        # return str(self.text).encode('utf-8', errors='replace')
        return self.text


class Answer(models.Model):
    text = models.TextField()
    isAnswer = models.BooleanField(default=False)
    userAnswer = False
    def __str__(self):
        # return str(self.text).encode('utf-8', errors='replace')
        return self.text



class Task(models.Model):
    question = models.ForeignKey(Question, blank=True, null=True)
    options = models.ManyToManyField(Answer, blank=True, related_name='options')
    answer_count = models.IntegerField(default=0)
    # answers = models.ManyToManyField(Answer, blank=True, related_name='answers')

    def __str__(self):
        # return str(self.question.text).encode('utf-8', errors='replace')
        return self.question.text



class Variant(models.Model):
    name = models.CharField(max_length=140, default='Вариант')
    tasks = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.TextField()
    variants = models.ManyToManyField(Variant, blank=True)

    def __str__(self):
        return self.name
