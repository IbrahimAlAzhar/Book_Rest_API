from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
