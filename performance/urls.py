from django.urls import path
from . import views

urlpatterns = [
    path('', views.performance_list, name='performance_list'),
    path('performance/', views.performance_list, name='performance_list'),
]
