from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'workStatus'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', auth_views.LoginView.as_view(template_name='workStatus/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name=''), name='logout'),
    path('status/', views.work_status, name='workStatus'),
    path('calendar/', views.work_calendar, name='workCalendar'),
]
