from django.urls import path

from . import views

app_name = 'workStatus'
urlpatterns = [
  path('', views.index, name='index'),
]