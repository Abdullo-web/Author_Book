
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),

    path('authors', authors, name='authors'),
    path('acreate', author_create, name='author_create'),
    path('adetail/<int:id>', author_detail, name='author_detail'),
    path('books', books, name='books'),
    path('createb', book_create, name='book_create'),
    path('bdetail/<int:id>', book_detail, name='book_detail'),
    path('update/<int:id>', book_update, name='book_update'),
    path('delete/<int:id>', book_delete, name='book_delete'),
]

