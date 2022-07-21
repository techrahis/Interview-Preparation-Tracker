from django.db import models


class Question_Attempted(models.Model):
    user = models.TextField(max_length=64)
    attempted_question_qIdentifier = models.CharField(max_length=64)

    class Meta:
        unique_together = (("user", "attempted_question_qIdentifier"),)
