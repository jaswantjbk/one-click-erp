from django.shortcuts import render
from .models import InventoryItem

def inventory_home(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory.html', {'items': items})
