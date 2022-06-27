from django.db import models
from topic.models import*
from category.models import*
# Create your models here.

class Question(models.Model):
    questionID = models.AutoField(primary_key=True)
    chooseCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    chooseTopic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    questionName = models.TextField()
    questionView = models.URLField(max_length=300)
    
    def __str__(self):
        return  self.chooseCategory.categoryName + "--"+ self.chooseTopic.topicName  + "--" + self.questionName
    