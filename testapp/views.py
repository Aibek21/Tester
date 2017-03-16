from django.http import HttpResponse
from .models import Question
from .models import Answer
from .models import Task
import re
from django.conf import settings
import os
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    return render(request, 'testapp/index.html')


def clear(request):
    Task.objects.all().delete()
    Question.objects.all().delete()
    Answer.objects.all().delete()
    return HttpResponse("Clear")


def parse(request):
    file_ = open(os.path.join(settings.BASE_DIR, 'testapp/file.txt'))
    content = file_.read()
    questions = re.split("#[0-9]+", content)

    for i, t in enumerate(questions):
        task = Task()
        # task question
        question_str = re.findall('\*!.+', t)
        if len(question_str) > 0:
            q = re.sub(r'\*!(\s+)?', '', question_str[0])
            question = Question()
            question.text = q
            if question is not None:
                question.save()
                task.question = question

        if task.question is not None:
            task.save()

            # options
            options_str = re.findall('\*[^!].+', t)
            for o in options_str:
                ans = Answer()
                if '*+' not in o:
                    o = re.sub(r'\*\+?(\s+)?', '', o)
                    ans.text = o
                    ans.save()
                else:
                    o = re.sub(r'\*\+?(\s+)?', '', o)
                    ans.text = o
                    ans.save()
                    task.answers.add(ans)

                task.options.add(ans)

            if task.question is not None and task.options.count() > 0:
                task.save()
    return HttpResponse("Parse")
