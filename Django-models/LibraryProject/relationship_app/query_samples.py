import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(f"Book Title: {book.title}")

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Book Title:{book.title}")

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian: {librarian.name}")

if __name__== '__main__':
    get_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Libray")