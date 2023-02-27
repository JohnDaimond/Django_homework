from django.urls import path
from .views import UserList, BookList, AuthorList, GenreList


urlpatterns = [
    path("users/", UserList.as_view(), name="api-users"),
    path("books/", BookList.as_view(), name="api-books"),
    path("authors/", AuthorList.as_view(), name="api-authors"),
    path("genres/", GenreList.as_view(), name="api-genres"),

]