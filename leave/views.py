from django.shortcuts import render, redirect
from .forms import LeaveRequestForm
from .models import LeaveRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.exceptions import ValidationError

@login_required
def submit_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        leave = form.save(commit=False)
        leave.user = request.user
        leave.status = 'hod_pending'
        leave.save()
        return redirect('leave_request_list')
    else:
        form = LeaveRequestForm(initial={'start_date': datetime.now().date()})
    return render(request, 'leave/leave_request_form.html', {'form': form})

@login_required
def leave_request_list(request):
    # Only show the current user's requests if they're not HR or HOD
    user_groups = [group.name for group in request.user.groups.all()]
    
    if 'HR' in user_groups or 'HOD' in user_groups:
        # HR and HOD can see all requests
        requests = LeaveRequest.objects.all().order_by('-submitted_at')
    else:
        # Regular employees only see their own requests
        requests = LeaveRequest.objects.filter(user=request.user).order_by('-submitted_at')
        
    return render(request, 'leave/leave_request_list.html', {'requests': requests})

@login_required
def approve_leave(request, pk, role):
    leave = LeaveRequest.objects.get(pk=pk)
    
    # Check permissions based on user groups
    user_groups = [group.name for group in request.user.groups.all()]
    
    # HOD moves from submitted to hod_pending, then approves/rejects
    if role == 'hod' and leave.status == 'submitted' and 'HOD' in user_groups:
        leave.status = 'hod_pending'
        leave.save()
        messages.info(request, 'Leave request is now pending HOD review.')

    if role == 'hod' and leave.status == 'hod_pending' and 'HOD' in user_groups:
        leave.status = 'hod_approved'
        leave.save()
        messages.success(request, 'Leave request approved by HOD.')

    if role == 'hod_reject' and leave.status in ['submitted', 'hod_pending'] and 'HOD' in user_groups:
        leave.status = 'hod_rejected'
        leave.save()
        messages.warning(request, 'Leave request rejected by HOD.')

    # HR approval (only HR can approve HR stage)
    if role == 'hr' and leave.status == 'hod_approved' and 'HR' in user_groups:
        leave.status = 'hr_approved'
        leave.save()
        messages.success(request, 'Leave request approved by HR.')
        
    return redirect('leave_request_list')
