from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book, YourModel
from .serializers import BookSerializer, YourModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class YourModelViewSet(ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    permission_classes = [IsAuthenticated]


