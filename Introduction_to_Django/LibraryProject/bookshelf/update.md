#Update Operation
```python
book = Book.objects.get(title="1948")
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

#Output
Nineteen Eighty-Four by George Orwell (1949)