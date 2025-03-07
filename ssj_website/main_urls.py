from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login-options/', views.login_options, name='login_options'),
    path('guest-login/', views.guest_login, name='guest_login'),
    path('guest-register/', views.guest_register, name='guest_register'),
    path('admin-login/', views.admin_login, name='admin_login'),
    # path('accounts/', include('allauth.urls')),  # Google Login URLs
]