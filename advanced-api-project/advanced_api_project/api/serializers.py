"""
Serializers
BookSerializer: Serializes all fields of Book. Includes validation to prevent future years.
AuthorSerializer: Serializes author name and includes a nested list of related books using BookSerializer.
This setup handles the one-to-many relationship from Author to Book using DRF's nested serializers.
"""


from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation ensures year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
# Author serializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']