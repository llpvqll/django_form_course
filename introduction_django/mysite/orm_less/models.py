from django.db import models

# Create your models here.


class Human(models.Model):

    CHOICE_COMPANY = (
        ('google', 'Google'),
        ('yandex', 'Yandex'),
        ('itvdn', 'Itvdn'),
        ('epam', 'Epam'),
    )

    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    birth = models.DateField(auto_now_add=False, auto_now=False)
    company = models.CharField(max_length=150, choices=CHOICE_COMPANY)
    salary = models.IntegerField()

    def __str__(self):
        return 'Имя  - {0} , Фамилия -  {1} , Компания - {2}'.format(self.name, self.surname, self.company)

    def dict(self):
        obj = {
            'name': self.name,
            'surname': self.surname,
            'birth': self.birth,
            'company': self.company,
            'salary': self.salary,
        }
        return obj

