from rest_framework import serializers
from products.models import Category, Manufacturer, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["slug", "name", "description"]


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["slug", "name"]


class ProductRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    manufacturer = ManufacturerSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "weight_kg", "pieces_per_package", "image", "manufacturer", "category"]


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "weight_kg", "pieces_per_package", "image", "manufacturer", "category"]
