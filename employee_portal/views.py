from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Attendance, Employee

def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'employee_login.html')

@login_required
def employee_dashboard(request):
    return render(request, 'dashboard/employee.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def gmail_view(request):
    user_email = request.user.email 
    if user_email:
        return redirect(f"https://mail.google.com/mail/u/{user_email}")
    return redirect("https://mail.google.com/")


@login_required
def calendar_view(request):
    return redirect("https://calendar.google.com/")


def user_logout(request):
    logout(request)
    return redirect('login_options')

@login_required
def sign_in(request):
    employee = Employee.objects.get(user=request.user)
    Attendance.objects.create(employee=employee, sign_in_time=now())
    return redirect('dashboard')

@login_required
def sign_out(request):
    employee = Employee.objects.get(user=request.user)
    attendance = Attendance.objects.filter(employee=employee, sign_out_time__isnull=True).last()
    if attendance:
        attendance.sign_out_time = now()
        attendance.save()
    return redirect('dashboard')
