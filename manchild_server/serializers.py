from rest_framework import serializers
from .models import Collection, CollectionItem

class CollectionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionItem
        fields = ["id", "name", "price_paid", "image", "manufacturer", "property", "created_at"]

class CollectionSerializer(serializers.ModelSerializer):
    items = CollectionItemSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ["id", "name", "description", "type", "created_at", "items"]