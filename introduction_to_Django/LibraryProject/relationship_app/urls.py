from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.index, name='index'),  # Sample URL
]
