from django.db import models
import datetime


class User(models.Model):
    login = models.CharField(max_length=15, unique=True)
    nick_name = models.CharField(max_length=15)
    email = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    avatar = models.CharField(max_length=50)


class Question(models.Model):
    user = models.ForeignKey(User)
    question_title = models.CharField(max_length=200)
    question_text = models.CharField(max_length=500)
    created = models.DateTimeField(default=datetime.datetime.now)
    rating = models.IntegerField()
    num_answers = models.IntegerField()
    tags = models.CharField(max_length=50)


# def __init__(self):
#		super(ClassName, self).__init__()
#		self.pub_date = datetime.datetime.datetime.datetime.now()


class Answers(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=500)
    isCorrect = models.BooleanField(default=False)
    rating = models.IntegerField()
    created = models.DateTimeField(default=datetime.datetime.now)

class Likes(models.Model):
    user = models.ForeignKey(User)
    likeType = models.CharField(max_length=10)
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answers)
