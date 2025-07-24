from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post', 'head', 'options']
    """
    Custom logout view that accepts both GET and POST requests.
    """
    template_name = 'registration/logged_out.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return render(request, self.template_name)

def logout_page(request):
    return render(request, 'registration/logged_out.html')
