from django.db import models

# Create your models here.


class Category(models.Model):
    categoryID = models.AutoField(primary_key=True)
    category_cIdentifier = models.CharField(max_length=64, unique=True)
    categoryName = models.CharField(max_length=200)

    def __str__(self):
        return self.categoryName
