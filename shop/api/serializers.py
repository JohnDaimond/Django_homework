from rest_framework import serializers
from django.contrib.auth.models import User
from catalog.models import Book, Author, Genre


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source="author.last_name")

    class Meta:
        model = Book
        fields = ['title', 'summary', 'publication_date', 'price', 'amount', 'genre', 'author', 'image', 'get_genre', 'author_name']



class AuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField(source='get_full_name')

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'



    class Meta:
        model = Author
        fields = ['full_name', 'first_name', 'last_name', 'date_of_birth', 'date_of_death', 'photo']



class GenreSerializer(serializers.ModelSerializer):
    #posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['name', 'genre_picture']

