from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventory
from .serializers import InventorySerializer

# Create your views here.
class InventoryView(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# class ItemView(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer