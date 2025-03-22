"""
BookListView with Advanced Query Capabilities:
- Filterable by: title, author (ID), publication_year
- Searchable by: title, author name (partial match)
- Orderable by: title, publication_year

Example Queries:
- /api/books/?publication_year=2023
- /api/books/?search=butler
- /api/books/?ordering=-publication_year
"""


from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# Create your views here.
# List all books (read-only)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering by field
    filterset_fields = ['title', 'publication_year', 'author']

    # Search functionality
    search_fields = ['title', 'author__name']  # supports nested field search

    # Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering


# Retrieve a single book by ID (read-only)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access

# Create a new book (requires authentication)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        # Custom hook (if needed later for logging, user assignment, etc.)
        serializer.save()

# Update an existing book (requires authentication)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Hook can be extended for tracking
        serializer.save()

# Delete a book (requires authentication)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


