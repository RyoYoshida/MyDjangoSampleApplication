from django.urls import path

from .views.polls.index import index
from .views.polls.detail import detail
from .views.polls.results import results
from .views.polls.vote import vote

from .views.polls.index import IndexView
from .views.polls.detail import DetailView
from .views.polls.results import ResultsView

app_name = "polls"
urlpatterns = [
    path("", index, name="index"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),

    path("index2", IndexView.as_view(), name="index2"),
    path("<int:pk>/detail2", DetailView.as_view(), name="detail2"),
    path("<int:pk>/results2/", ResultsView.as_view(), name="results2"),
]
