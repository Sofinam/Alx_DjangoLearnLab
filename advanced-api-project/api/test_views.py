from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")  # Optional for authenticated routes

        # Sample books
        self.book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
        self.book2 = Book.objects.create(title="Brave New World", author="Aldous Huxley", publication_year=1932)

    def test_list_books(self):
        url = reverse("book-list")  # Make sure this matches your url name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_detail(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book(self):
        self.client.logout()
        self.client.login(username="testuser", password="testpass")
        url = reverse("book-create")
        data = {
            "title": "Sapiens",
            "author": "Yuval Noah Harari",
            "publication_year": 2011
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Nineteen Eighty-Four",
            "author": "George Orwell",
            "publication_year": 1949
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        url = reverse("book-delete", args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        url = reverse("book-list") + "?publication_year=1949"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Brave"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Brave New World")

    def test_order_books_by_title_desc(self):
        url = reverse("book-list") + "?ordering=-title"
        response = self.client.get(url)
        self.assertEqual(response.data[0]["title"], "Brave New World")
