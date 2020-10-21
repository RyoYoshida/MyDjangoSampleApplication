from django.utils import timezone

# from polls.models import Answer
# from polls.models import Choice
from polls.models import Question


print(Question.objects.all())

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
print(q.id)
print(q.question_text)

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
print(q.id)
print(q.question_text)

q.question_text = "What's up?"
q.save()
print(q.id)
print(q.question_text)

print(Question.objects.all())
