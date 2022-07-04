from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.BookList, name='books'),
    path('book/<int:pk>', views.BookDetail, name='book-detail'),
    path('authors/', views.AuthorList, name='authors'),
    
]