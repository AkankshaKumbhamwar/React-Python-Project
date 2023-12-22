# from django.test import TestCase

# # Create your tests here.
# class Member(models.Model):
#   Topic = models.CharField(max_length=150)
#   Description = models.CharField(max_length=300)
#   by = models.CharField(max_length=150)
#   date = models.date()


# tests.py

from django.test import TestCase

class Member(models.Model):
    Topic = models.CharField(max_length=150)
    Description = models.CharField(max_length=300)
    by = models.CharField(max_length=150)
    date = models.DateField()
