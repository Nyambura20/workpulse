"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from .views import dashboard, logout_page, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Custom logout view that handles GET requests (must come before auth URLs)
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/logged_out/', logout_page, name='logout_page'),
    # Include auth URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('hr/', include('hr.urls')),
    path('employee/', include('employee.urls')),
    path('leave/', include('leave.urls')),
    path('hod/', include('hod.urls')),
    path('attendance/', include('attendance.urls')),
    path('performance/', include('performance.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]
