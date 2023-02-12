from django.contrib import admin
from django.urls import path
from .views import CatalogView, AuthorsView, AuthorCatalogView, BookView, SearchView


urlpatterns = [
    path("", CatalogView.as_view(), name="catalog-index"),
    path("catalog/book-<int:id>/", BookView.as_view(), name="catalog-book"),
    path("authors/", AuthorsView.as_view(), name="catalog-authors"),
    path("authors/<str:first_name>-<str:last_name>-<int:id>/", AuthorCatalogView.as_view(), name="catalog-authors-author"),
    path("catalog/search/", SearchView.as_view(), name="catalog-search")
]