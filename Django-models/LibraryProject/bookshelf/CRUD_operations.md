# Create Operation
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book) 

# Retrieve Operation

```python
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# delete Operation
book.delete()
print(Book.objects.all())

#Update Operation
book.title = "Nineteen Eighty-Four"
book.save()
print(book)