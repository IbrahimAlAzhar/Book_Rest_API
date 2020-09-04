# a serializer translates data into a format that is easy to consume over the internet,typically JSON,and is displayed
# at an API endpoint ,here create a serializer with Django Rest framework  to convert django models to JSON
from rest_framework import serializers
from books.models import Book


# here we extend django REST framework's ModelSerializer into a BookSerializer that specifies our database model,fields
class BookSerializer(serializers.ModelSerializer): # here create a serializer like model in traditional django,this serializer converts the data into json format
    class Meta:
        model = Book
        fields = ('title','subtitle','author','isbn')
