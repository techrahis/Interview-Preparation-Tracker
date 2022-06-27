from django.db import models

# Create your models here.
class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.TextField(max_length=150)
    
    def __str__(self):
        return self.categoryName