from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100)
    slug = models.CharField(max_length=300)
    
class Question(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=100)
    slug = models.CharField(max_length=200)