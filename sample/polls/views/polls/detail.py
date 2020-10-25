from django.utils import timezone
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

    def get_queryset(self):
        # Excludes any questions that aren't published yet.
        return Question.objects.filter(pub_date__lte=timezone.now())
