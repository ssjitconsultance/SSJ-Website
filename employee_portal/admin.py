from django.contrib import admin
from .models import Employee, GuestProfile, Attendance, Calendar, Email

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'department', 'position', 'date_joined')
    search_fields = ('employee_id', 'user__first_name', 'user__last_name', 'department')
    list_filter = ('department', 'date_joined')

@admin.register(GuestProfile)
class GuestProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'mobile')
    search_fields = ('user__first_name', 'user__last_name', 'company')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'sign_in_time', 'sign_out_time')
    list_filter = ('sign_in_time', 'sign_out_time')

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'employee', 'start_time', 'end_time', 'is_all_day')
    list_filter = ('is_all_day', 'start_time')

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')