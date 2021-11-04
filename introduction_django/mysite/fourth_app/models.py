from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthday = models.DateField()

    def __str__(self):
        return self.surname


class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    pages_count = models.IntegerField()
    date_of_publication = models.DateField()

    def __str__(self):
        return self.book_name






