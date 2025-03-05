#Update Operation
```python
book = Book.objects.get(title="Tom Sawyer")
book.title = "Tom Sawyer"
book.save()
print(book)

#Output
Tom Sawyer b Mark Twain (2002)