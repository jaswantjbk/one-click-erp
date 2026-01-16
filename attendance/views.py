from django.shortcuts import render
from .models import Attendance

def attendance_home(request):
    records = Attendance.objects.all()
    return render(request, 'attendance/attendance.html', {'records': records})
