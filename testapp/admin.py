from django.contrib import admin
from .models import Question
from .models import Answer
from .models import Task
from .models import Variant

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Task)
admin.site.register(Variant)
