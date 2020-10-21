from django.contrib import admin

from .models import Answer
from .models import Choice
from .models import Question

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
