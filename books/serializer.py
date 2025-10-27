from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
    def validate_price(self, stock):
        if stock < 0:
            raise serializers.ValidationError('Price cannot be negative.')
        return stock