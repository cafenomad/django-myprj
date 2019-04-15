# -*- coding: utf-8 -*-
"""books.urls."""

from django.conf.urls import url
from books.views.book import BookListView
from books.views.book import BookDetailView


app_name = 'books'
urlpatterns = [
    path('',
         BookListView.as_view(),
         name='book'),

    path('book/<int:book_id>/',
         BookDetailView.as_view(),
         name='book_detail'),
]
