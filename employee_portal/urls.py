from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.employee_login, name='employee_login'),
    path('dashboard/', views.employee_dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('gmail/', views.gmail_view, name='gmail'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('logout/', views.user_logout, name='logout'),
]
