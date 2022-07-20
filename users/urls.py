""" Defines schemas URL for  users """

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # On default URL authorization
    path('', include('django.contrib.auth.urls')),
    # Page of registration
    path('register/', views.register, name='register'),
]

