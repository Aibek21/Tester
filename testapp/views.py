# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Question, Answer, Task, Variant, Course
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import re
from django.conf import settings
import os
from django.shortcuts import render, get_object_or_404, redirect
from . import telegram


def index(request):
    courses = Course.objects.values('pk', 'name')
    return render(request, 'testapp/index.html', {'courses': courses})

def variant_list(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'testapp/variant_list.html', {'course': course.name,'variants': course.variants.all()})


def variant_detail(request, pk):
    variant = get_object_or_404(Variant, pk=pk)
    taskList = variant.tasks.all()

    return render(request, 'testapp/variant_detail.html',
                  {'variant': variant, 'tasks': taskList, })


def test_result(request):
   
    pp = request.POST;
    pk = request.POST.get("pk", "");
    variant = get_object_or_404(Variant, pk=pk)


    taskList = []
    answerList = dict()

    aa = None
    correct = 0
    for task in variant.tasks.all():
        if str(task.pk) in pp:
            answerList[task.pk] = []
            answerList[task.pk] = pp.getlist(str(task.pk))
            for item in answerList[task.pk]:
                a=1
        taskList.append(task)

    for task in variant.tasks.all():
        answer_count = 0
        correct_count = 0
        for option in task.options.all():
            if option.isAnswer:
                answer_count+=1
                if task.pk in answerList:
                    for item in answerList[task.pk]:
                        if str(option.pk)==item:
                            correct_count+=1
        if task.pk in answerList and correct_count==len(answerList[task.pk]) and answer_count==correct_count:
            correct+=1        


    all_ids = []
    updates = telegram.get_updates()
    for update in updates["result"]:
        chat = update["message"]["chat"]["id"]
        all_ids.append(chat)
    user_ids = set(all_ids)
    for idm in set(user_ids):
        text = str(variant.name) + ' Result: ' +  str(correct)
        telegram.send_message(text, idm)


    return render(request, 'testapp/result.html',
                  {'total':len(taskList), 
                  'correct': correct,
                  'variant': variant.name, 
                  'result': taskList,
                  'answerList': answerList})



def clear(request):
    Course.objects.all().delete()
    Variant.objects.all().delete()
    Task.objects.all().delete()
    Question.objects.all().delete()
    Answer.objects.all().delete()
    return HttpResponse("Clear")


def parse(request):
    file_ = open(os.path.join(settings.BASE_DIR, 'testapp/courses.txt'))
    content = file_.readlines()

    for s in content:
        ss = re.split(";", s.rstrip('\n'))
        file_ = open(os.path.join(settings.BASE_DIR, 'testapp/'+ss[1]))
        course_content = file_.read()
        tasks = []
        questions = re.split("#[0-9]+", course_content)
        course = Course()
        course.name = ss[0]
        course.save()
        for i, t in enumerate(questions):
            task = Task()
            # task question
            question_str = re.findall('\*!.+\n?.+', t)
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
                answer_count = 0
                for o in options_str:
                    ans = Answer()
                    
                    if '*+' not in o:
                        ans.isAnswer = False
                    else:
                        ans.isAnswer = True
                        answer_count+=1

                    o = re.sub(r'\*\+?(\s+)?', '', o)
                    ans.text = o
                    ans.save()
                    # task.answers.add(ans)
                    task.options.add(ans)
                task.answer_count = answer_count
                # if answer_count == 0:
                #     print task.question
                if task.question is not None and task.options.count() > 0:
                    task.save()
                    tasks.append(task)


        counter = 0
        variantNo = 1
        while counter < len(tasks):
            variant = Variant()
            variant.name = "Variant {}".format(variantNo)
            variant.save()
            for j in range(0, 40, 1):
                if counter < len(tasks):
                    variant.tasks.add(tasks[counter])
                    counter += 1

            variant.save()
            variantNo += 1
            course.variants.add(variant)
        course.save()


    return HttpResponse("Parse")


