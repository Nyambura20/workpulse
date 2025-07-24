from django.shortcuts import render
from .models import PerformanceRecord

def performance_list(request):
    records = PerformanceRecord.objects.all()
    return render(request, 'performance/performance_list.html', {'records': records})
