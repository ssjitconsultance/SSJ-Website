from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from employee_portal.models import GuestProfile

def home(request):
    return render(request, 'home.html')

def login_options(request):
    return render(request, 'login_options.html')

def guest_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if GuestProfile.objects.filter(user=user).exists():
                login(request, user)
                messages.success(request, f"Welcome back, {user.get_full_name()}!")
                return redirect('home')
            messages.error(request, "This account is not registered as a guest.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'guest_login.html')

def guest_register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=email).exists():
            messages.error(request, "A user with this email already exists.")
            return render(request, 'guest_register.html')
        first_name, last_name = (full_name.split(' ', 1) + [''])[:2]
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        GuestProfile.objects.create(user=user, mobile=mobile)
        login(request, user)
        messages.success(request, "Registration successful! Welcome to SSJ IT Consultancy.")
        return redirect('home')
    return render(request, 'guest_register.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, f"Welcome, Admin {user.get_full_name()}!")
            return redirect('/admin/')
        messages.error(request, "Invalid admin credentials.")
    return render(request, 'admin_login.html')
def custom_redirect_after_login(request):
    user = request.user
    if user.is_superuser:  # Admin user
        return redirect('/admin/')
    elif user.groups.filter(name='Guest').exists():
        return redirect('guest_dashboard')  # Redirect guests
    else:
        return redirect('dashboard')  # Default for employees