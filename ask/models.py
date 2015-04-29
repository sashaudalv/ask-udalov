from django.db import models
from django.contrib.auth.models import User
import datetime

class CustomUser(User):
    avatar = models.ImageField()
    rating = models.IntegerField(default=0)


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)


class Question(models.Model):
    user_ptr = models.ForeignKey(CustomUser)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.now)
    rating = models.IntegerField(default=0)
    num_answers = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)


class Answer(models.Model):
    user_ptr = models.ForeignKey(CustomUser)
    question = models.ForeignKey(Question)
    text = models.TextField()
    isCorrect = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.datetime.now)


class QuestionLike(models.Model):
    user_ptr = models.ForeignKey(CustomUser)
    likeType = models.IntegerField(default=0) #can be -1, 0, 1
    question = models.ForeignKey(Question)
    class Meta:
        unique_together = ('user_ptr', 'question',)


class AnswerLike(models.Model):
    user_ptr = models.ForeignKey(CustomUser)
    likeType = models.IntegerField(default=0)
    answer = models.ForeignKey(Answer)
    class Meta:
        unique_together = ('user_ptr', 'answer',)


# class UserLike(models.Model):
#     user = models.ForeignKey(User)
#     likeType = models.IntegerField(default=0)
#     anotherUser = models.ForeignKey(User)
#     class Meta:
#         unique_together = ('user', 'anotherUser',)




