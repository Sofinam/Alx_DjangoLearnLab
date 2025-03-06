# Delete Operation

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted successfully.")

# Output
Book deleted successfully.
