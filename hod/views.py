from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from leave.models import LeaveRequest
from django.contrib import messages

def is_hod(user):
    return user.groups.filter(name='HOD').exists()

@login_required
@user_passes_test(is_hod)
def hod_dashboard(request):
    return render(request, 'hod/dashboard.html')

@login_required
@user_passes_test(is_hod)
def pending_requests(request):
    requests = LeaveRequest.objects.filter(status='hod_pending')
    return render(request, 'hod/pending_requests.html', {'requests': requests})

@login_required
@user_passes_test(is_hod)
def approve_request(request, pk):
    leave = get_object_or_404(LeaveRequest, pk=pk)
    leave.status = 'hod_approved'
    leave.save()
    return redirect('hod_pending_requests')

@login_required
@user_passes_test(is_hod)
def reject_request(request, pk):
    leave = get_object_or_404(LeaveRequest, pk=pk)
    leave.status = 'hod_rejected'
    leave.save()
    return redirect('hod_pending_requests')