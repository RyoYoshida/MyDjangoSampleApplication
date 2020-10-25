from django.utils import timezone
from django.views import generic
from django.shortcuts import render

from ...models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Return the last five published questions (not including those set to be published in the future).
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
