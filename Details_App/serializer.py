from rest_framework import serializers
from . import models

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Genre

class subGenreSerializer(serializers.ModelSerializer):
    sungen=GenreSerializer(source = 'genre')
    class Meta:
        fields='__all__'
        model=models.SubGenre

class AuthorSerializer(serializers.ModelSerializer):
    auth=subGenreSerializer(source='subGen')
    class Meta:
        fields = '__all__'
        model = models.Author

class BookSerializer(serializers.ModelSerializer):
    book = AuthorSerializer(source = 'author')

    class Meta:
        fields = '__all__'
        model = models.Book

