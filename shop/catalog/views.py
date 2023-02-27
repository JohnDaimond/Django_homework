from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author, Genre
from cart.models import Cart

class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"


    def get(self, request):
        try:
            Cart.objects.get(user=request.user)
        except:
            try:
                Cart.objects.create(user=request.user)
            except:
                print('User is anonymous')

        books = Book.objects.all()
        genres = Genre.objects.all()

        params = {
            'title': "All",
            'books': books,
            'genres': genres
        }

        return render(request, self.template_name, params)

class BookView(TemplateView):
    template_name = "catalog/book.html"

    def get(self, request, id):
        book = Book.objects.get(id=id)
        genres = Genre.objects.all()

        params = {
            'title': f"{book.title} detail",
            'book': book,
            'genres': genres
        }

        return render(request, self.template_name, params)


class AuthorsView(TemplateView):
    template_name = "catalog/authors.html"

    def get(self, request):
        authors = Author.objects.all()
        genres = Genre.objects.all()

        params = {
            'authors': authors,
            'genres': genres
        }

        return render(request, self.template_name, params)


class AuthorCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, first_name, last_name, id):
        author = Author.objects.get(id=id)
        books = Book.objects.filter(author=author)
        genres = Genre.objects.all()

        params = {
            'title': f"{last_name}'s",
            'author': author,
            'books': books,
            'genres': genres
        }

        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = "catalog/catalog.html"

    def post(self, request):
        search = request.POST['search']
        genres = Genre.objects.all()
        books_by_title = Book.objects.filter(title__icontains=search)
        books_by_summary = Book.objects.filter(summary__icontains=search)
        books_by_dop = Book.objects.filter(date_of_publication__icontains=search)
        books_by_price = Book.objects.filter(price__icontains=search)
        books_by_author_last_name = Book.objects.filter(author__last_name__icontains=search)
        books_by_author_first_name = Book.objects.filter(author__first_name__icontains=search)

        books = books_by_title.union(books_by_dop,books_by_price,books_by_summary, books_by_author_first_name,books_by_author_last_name, all=False)
        params = {
            'books': books,
            'title': f"'{search}'",
            'genres': genres
        }

        return render(request, self.template_name, params)

class GenreCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, id):
        genre = Genre.objects.get(id=id)
        books = Book.objects.filter(genre=genre)
        genres = Genre.objects.all()

        params = {
            'title': f"{genre.name}'s",
            'books': books,
            'genres': genres
        }

        return render(request, self.template_name, params)
