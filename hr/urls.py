from django.urls import path
from .views import hr_dashboard

urlpatterns = [
    path('dashboard/', hr_dashboard, name='hr_dashboard'),
]
