from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='list/', permanent=False)),
    path('request/', views.submit_leave_request, name='submit_leave_request'),
    path('list/', views.leave_request_list, name='leave_request_list'),
    path('approve/<int:pk>/<str:role>/', views.approve_leave, name='approve_leave'),
]
