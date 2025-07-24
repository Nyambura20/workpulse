from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_hr(user):
    return user.groups.filter(name='HR').exists()

@login_required
@user_passes_test(is_hr)
def hr_dashboard(request):
    return render(request, 'hr/dashboard.html')
