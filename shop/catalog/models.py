from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="authors/", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    def get_author_url(self):
        return reverse("catalog-authors-author", args=[self.first_name, self.last_name, self.id])


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField()
    summary = models.TextField()
    publication_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, default=1.00, decimal_places=2)
    amount = models.IntegerField(null=False)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    image = models.ImageField(upload_to="books/", blank=True, default="book-placeholder.jpeg")

    def __str__(self):
        return f"{self.title} {self.summary} {self.publication_date} {self.price} {self.amount}"

    def get_genre(self):
        return ", ".join([genre.name for genre in self.genre.all()])

    def get_date(self):
        return self.publication_date.strftime("%Y")

    def get_book_url(self):
        return reverse("catalog-book", args=[self.id])

    get_genre.short_description = "Genre"