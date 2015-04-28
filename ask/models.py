from django.db import models
import datetime


class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    nick_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    avatar = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)


class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    created = models.DateTimeField(default=datetime.datetime.now)
    rating = models.IntegerField(default=0)
    num_answers = models.IntegerField(default=0)


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=500)
    isCorrect = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.datetime.now)


class QuestionLike(models.Model):
    user = models.ForeignKey(User)
    likeType = models.IntegerField(default=0) #can be -1, 0, 1
    question = models.ForeignKey(Question)
    class Meta:
        unique_together = ('user', 'question',)


class AnswerLike(models.Model):
    user = models.ForeignKey(User)
    likeType = models.IntegerField(default=0)
    answer = models.ForeignKey(Answer)
    class Meta:
        unique_together = ('user', 'answer',)


# class UserLike(models.Model):
#     user = models.ForeignKey(User)
#     likeType = models.IntegerField(default=0)
#     anotherUser = models.ForeignKey(User)
#     class Meta:
#         unique_together = ('user', 'anotherUser',)


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    questions = models.ManyToManyField(Question)

