""" Defines schemas URL for  users """

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # On default URL authorization
    path('', include('django.contrib.auth.urls')),
]

