#Create Operation
```python
from bookshelf .models import Book
book = Book.objects.create(title="Tom Sawyer", author="Mark Twain", publication_year="2002")
print(book)

#Output
Tom Sawyer b Mark Twain (2002)