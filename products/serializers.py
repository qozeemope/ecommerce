from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    category_name = serializers.ReadOnlyField(source="category.name")
    
    class Meta:
        model = Product
        fields = [
            "id",
            "owner",
            "name",
            "description",
            "price",
            "category",
            "category_name",
            "stock_quantity",
            "image_url",
            "created_at",
        ]
        read_only_fields = ["id", "owner", "created_at", "category_name"]

    def validate_price(self, value):
        if value is None:
            raise serializers.ValidationError("Price is required.")
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_stock_quantity(self, value):
        if value is None:
            raise serializers.ValidationError("Stock quantity is required.")
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value
    
    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Name is required.")
        return value.strip()