from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='pending/', permanent=False)),
    path('pending/', views.pending_requests, name='hod_pending_requests'),
    path('approve/<int:pk>/', views.approve_request, name='hod_approve_request'),
    path('reject/<int:pk>/', views.reject_request, name='hod_reject_request'),
]