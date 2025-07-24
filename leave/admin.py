from django.contrib import admin
from .models import LeaveRequest

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'status', 'submitted_at')
    list_filter = ('status', 'start_date')
    search_fields = ('user__username', 'reason')
    date_hierarchy = 'submitted_at'
