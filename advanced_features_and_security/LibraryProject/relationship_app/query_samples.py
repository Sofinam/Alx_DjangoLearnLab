import os
import django

#setting up Django environment
os.environ.setdefault('DJANGO_STTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

#Querying all books
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(book.title)

#List all books in the Library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}:")
    for book in books:
        print(book.title)

#Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library_name}: {librarian.name}")

#Run the queries
if __name__ == "__main__":
    get_books_by_author("J.K. Rowling")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
     