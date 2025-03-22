from django.db import models
from django.utils import timezone

"""
Models:
Author which represents a book author with a name.
Book represents a book with a title, publication year
Foreignkey from book to Author establishes a one to many relationship
"""


# Create your models here.
#Represents book author
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title ({self.publication_year})}"
