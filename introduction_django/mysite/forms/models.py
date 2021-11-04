from django.db import models

# Create your models here.


class Human(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.DateField()
    company = models.CharField(max_length=50)
    salary = models.IntegerField()


