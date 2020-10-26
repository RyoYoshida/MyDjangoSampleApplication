from django.contrib import admin

from .models import Answer
from .models import Choice
from .models import Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 2


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = []
    inlines = [AnswerInline]


admin.site.register(Choice, ChoiceAdmin)


admin.site.register(Answer)
