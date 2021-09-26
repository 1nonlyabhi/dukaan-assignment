from rest_framework import serializers

from store.models import Product, Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'address', 'slug']
        extra_kwargs = {
            'id': {'read_only': True},
            'slug': {'read_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'mrp', 'sale_price', 'image', 'category']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class GroupSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'category']
        extra_kwargs = {
            'id': {'read_only': True},
        }