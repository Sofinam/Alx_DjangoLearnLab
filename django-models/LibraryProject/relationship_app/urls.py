from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register_view, admin_view, librarian_view, member_view, add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("register/", register_view, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    #role based urls
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),

    #Book Management urls
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]