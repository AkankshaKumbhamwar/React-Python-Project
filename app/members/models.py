from django.db import models

class Member(models.Model):
  Topic = models.CharField(max_length=150)
  Description = models.CharField(max_length=300)
  By = models.CharField(max_length=150)
  Date = models.DateField()