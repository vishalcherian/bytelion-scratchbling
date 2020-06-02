from django.shortcuts import render
from django.http import HttpResponse
from api.models import Inventory

def home(request):
    context = {
        'inventory': Inventory.objects.all()
    }
    print(context)
    return render(request, 'home.html', context)
