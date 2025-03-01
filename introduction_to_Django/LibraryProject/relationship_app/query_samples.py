import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None

# Testing Queries
if __name__ == "__main__":
    # Sample queries
    author_books = get_books_by_author("J.K. Rowling")
    print(f"Books by J.K. Rowling: {[book.title for book in author_books]}")

    library_books = get_books_in_library("Central Library")
    print(f"Books in Central Library: {[book.title for book in library_books]}")

    librarian = get_librarian_for_library("Central Library")
    if librarian:
        print(f"Librarian of Central Library: {librarian.name}")
    else:
        print("No librarian found for Central Library.")
