"""
Models:
- Author: Represents an author with a name.
- Book: Represents a book with a title, publication year, and foreign key to Author.
The Author-to-Book relationship is one-to-many via ForeignKey.
"""

from django.db import models

# Create your models here.

# Author model stores names of book authors.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model stores book details and links each book to an Author via ForeignKey.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"