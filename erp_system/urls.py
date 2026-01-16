from django.contrib import admin
from django.urls import path
from core.views import dashboard
from attendance.views import attendance_home
from inventory.views import inventory_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('attendance/', attendance_home, name='attendance'),
    path('inventory/', inventory_home, name='inventory'),
]

