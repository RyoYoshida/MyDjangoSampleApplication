from django.shortcuts import get_object_or_404
from django.shortcuts import render

from ...models import Question


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
