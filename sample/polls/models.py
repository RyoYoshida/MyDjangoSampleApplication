from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=191)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=191)
    votes = models.IntegerField(default=0)


class Answer(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
