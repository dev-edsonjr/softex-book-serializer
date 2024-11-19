from rest_framework import serializers
from books.models import Book
from decimal import Decimal

class BookSerializer(serializers.ModelSerializer):
    # Campo calculado para o preço em dólares
    price_in_dollars = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'price_in_dollars', 'pages']

    # Método para calcular o valor do campo price_in_dollars
    def get_price_in_dollars(self, obj):
        return round(obj.price / Decimal('5.77'), 2)
