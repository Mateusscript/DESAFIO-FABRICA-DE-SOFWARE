from rest_framework import viewsets
from books.api import serializers
from books import models

class booksviewset(viewsets.ModelViewSet):
    serializer_class=serializers.booksserializer
    queryset = models.boocks.objects.all()