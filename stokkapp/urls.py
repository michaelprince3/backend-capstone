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
    path('newform', new_user_item_form, name='new_user_item_form'),
    path('item/<int:user_item_id>/edit',
         user_item_edit_form, name='user_item_edit_form'),
    path('items', user_item_list, name='user_item_list'),
    path('detail/<int:user_item_id>', user_item_details, name='detail'),
    path('shoppinglist/', shopping_list, name='shoppinglist'),
    path('listitem/<int:user_item_id>', shopping_list_item, name='shopping_list_item')

]
