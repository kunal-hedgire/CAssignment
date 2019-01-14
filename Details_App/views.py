from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import *
from .serializer import BookSerializer

class get_Book(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class = BookSerializer

