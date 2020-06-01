from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'item_name', 'item_description', 'item_size','item_cost')

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = ('item_name', 'item_size')