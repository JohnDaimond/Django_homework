from django.contrib import admin
from .models import Book, Author, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "publication_date", "price", "amount", "author", "get_genre")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth", "date_of_death", "photo")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass