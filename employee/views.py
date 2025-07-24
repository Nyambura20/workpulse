from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def is_employee(user):
    return user.groups.filter(name='Employee').exists()

@login_required
@user_passes_test(is_employee)
def employee_dashboard(request):
    return render(request, 'employee/dashboard.html')
