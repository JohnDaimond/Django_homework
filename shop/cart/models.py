from django.db import models
from catalog.models import Book
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="cart")
    products = models.ManyToManyField(Book, blank=True)


    def get_total_price(self):
        return sum([book.price for book in self.products.all()])

    def get_total_quantity(self):
        return len([book for book in self.products.all()])

    def display_products(self):
        return ", ".join([book.title for book in self.products.all()])