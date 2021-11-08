from django.db import models

# Create your models here.


class Human(models.Model):
    name = models.CharField(max_length=30, verbose_name='User name')
    surname = models.CharField(max_length=30, verbose_name='User surname')
    age = models.DateField(verbose_name='Birthday date')
    company = models.CharField(max_length=50, verbose_name='Company name')
    salary = models.IntegerField(verbose_name='Your salary')

    def __str__(self):
        return self.surname

