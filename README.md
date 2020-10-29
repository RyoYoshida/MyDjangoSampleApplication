# MyDjangoApplication
## Reference
- https://docs.djangoproject.com/ja/3.1/intro/tutorial01/

## Initialization
```
django-admin startproject sample

cd sample/
python3 manage.py runserver

python3 manage.py startapp polls

python3 manage.py migrate

python3 manage.py makemigrations polls
python3 manage.py sqlmigrate polls 0001
python3 manage.py migrate

python3 manage.py createsuperuser

cat polls/question.py |  python3 manage.py shell
python3 manage.py test polls
```
