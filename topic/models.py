from django.db import models
from home.models import*
# Create your models here.
class Topic(models.Model):
    topicID = models.AutoField(primary_key=True)
    topicName = models.CharField(max_length=200)

    def __str__(self):
        return self.topicName