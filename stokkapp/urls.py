from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from .views import *


app_name = 'stokkapp'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('', home, name='home'),
]