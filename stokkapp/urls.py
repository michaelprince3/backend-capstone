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
    path('form/', user_item_form, name='user_item_form'),
    path('items', user_item_list, name='user_item_list'),
    path('detail/<int:user_item_id>', user_item_details, name='detail')

]
