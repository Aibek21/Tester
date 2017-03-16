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
        # return self.question.text.encode('utf-8', errors='replace')
        return 'Вариант {}'.format(self.pk)

    def toString(self):
        print self.question.text.encode('utf-8', errors='replace')
        # for o in self.options:
        #     print '\t' * 2, o
        #
        # for a in self.answers:
        #     print '\t answers: ', a


class Variant(models.Model):
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return 'Вариант {}', self.self.pk
