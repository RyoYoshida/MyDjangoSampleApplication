from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import generic

from ...models import Question


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
