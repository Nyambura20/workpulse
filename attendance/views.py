from django.shortcuts import render
from .models import AttendanceRecord

def attendance_list(request):
    records = AttendanceRecord.objects.all()
    return render(request, 'attendance/attendance_list.html', {'records': records})
