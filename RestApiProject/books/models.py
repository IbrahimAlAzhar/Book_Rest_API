from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)  # ISBN is a unique,13-character identifier assigned to every published book

    def __str__(self):  # we include a __str__ method so that the title of a book will display in the admin later on
        return self.title