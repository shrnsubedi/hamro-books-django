from django.urls import path
from .views import (
    BookListView,
    BookUpdateView,
    BookDeleteView,
    BookDetailView,
    BookCreateView,
    SpeakCreateView,
    BookFilterListView,
    BookSearchListView
)

urlpatterns = [
    path("<int:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("new/", BookCreateView.as_view(), name="book_create"),
    path("<int:pk>/speak/", SpeakCreateView.as_view(), name="speak_post"),
    path("", BookListView.as_view(), name="book_list"),
    path("<genre>",BookFilterListView.as_view(),name="book_filter"),
    path("search/",BookSearchListView.as_view(),name="book_search"),


]

