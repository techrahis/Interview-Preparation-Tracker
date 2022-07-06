from django.db import models
from home.models import*
# Create your models here.


class Topic(models.Model):
    topicID = models.AutoField(primary_key=True)
    topic_cIdentifier = models.CharField(max_length=64)
    topic_tIdentifier = models.CharField(max_length=64, unique=True)
    topicName = models.CharField(max_length=200)

    def __str__(self):
        return self.topicName
