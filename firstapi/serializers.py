from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length= 100)
    description = serializers.CharField()

    
    class Meta:
        model = Book
        fields = ('title', 'description')