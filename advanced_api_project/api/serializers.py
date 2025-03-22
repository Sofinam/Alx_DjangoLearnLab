"""sumary_line
Serializers:
BookSerializer: It serializers all fields in book model including custom validation
AuthorSerializer: It serializes the author name including nested serialisation of realted book instances
Relationship between Author and Book is one to many. Each book is linked to one Author and each Author can have many books
Return: return_description
"""


from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    #Custom validation
    def validate_publication_year(self, value):
        current_year = datetime.now() .year
        if value > current_year:
            raise serializers.ValidateError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']