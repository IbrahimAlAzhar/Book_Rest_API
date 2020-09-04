from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer # import serializer from api app,here BookSerializer comes from serializers.py file(it acts like a model)

# some developers will create an API views file like 'apiviews.py' in views.py file in as same directory where other
# codes are,but in here we create a separate app so don't create confusion here


# we create a BookAPIView that uses ListAPIView to create a read-only endpoint for all book instances,we don't need to template in rest api
class BookAPIView(generics.ListAPIView):  # here inherits from ListAPIView to list all book
    queryset = Book.objects.all()  # take all objects and store it to queryset variable
    serializer_class = BookSerializer  # define the serializer_class which will be BookSerializer,here BookSerialzier acts like a model here it works to convert django model to JSON
