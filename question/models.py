from django.db import models
from topic.models import*
from category.models import*


class Question(models.Model):
    questionID = models.AutoField(primary_key=True)
    question_cIdentifier = models.CharField(max_length=64)
    question_tIdentifier = models.CharField(max_length=64)
    question_qIdentifier = models.CharField(max_length=64)
    questionName = models.CharField(max_length=200)
    questionLink = models.URLField(max_length=300)

    def __str__(self):
        return self.questionName
