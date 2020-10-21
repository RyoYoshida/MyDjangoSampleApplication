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


# Django provides a rich database lookup API that's entirely driven by keyword arguments.
print(Question.objects.filter(id=1))
print(Question.objects.filter(question_text__startswith='What'))

# Get the question that was published this year.
from django.utils import timezone
current_year = timezone.now().year
print(Question.objects.filter(pub_date__year=current_year))

# Request an ID that doesn't exist, this will raise an exception.
print(Question.objects.get(id=2))

# Lookup by a primary key is the most common case, so Django provides a shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
print(Question.objects.get(pk=1))

# Make sure our custom method worked.
q = Question.objects.get(pk=1)
print(q.was_published_recently())

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
print(q.choice_set.all())

# Create three choices.
print(q.choice_set.create(choice_text='Not much', votes=0))
print(q.choice_set.create(choice_text='The sky', votes=0))
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
print(c.question)

# And vice versa: Question objects get access to Choice objects.
print(q.choice_set.all())
print(q.choice_set.count())
