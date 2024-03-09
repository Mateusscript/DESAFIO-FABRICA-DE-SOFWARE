from rest_framework import serializers
from books import models

class booksserializer(serializers.ModelSerializer):
    class Meta:
        model = models.boocks
        fields = '__all__'