from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Function based view which lists all books with their authors
def book_list(request):
    books = Book.objects.all()
    book_details = "\n" .join([f"{Book.title} by {Book.author.name}" for books in books])
    return HttpResponse(f"<pre>{book_details}</pre>")

#Class-based view, displays details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"