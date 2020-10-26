from django.urls import path

from .views.polls.index import index
from .views.polls.detail import detail
from .views.polls.results import results
from .views.polls.vote import vote

urlpatterns = [
    path("", index, name="index"),
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
]
