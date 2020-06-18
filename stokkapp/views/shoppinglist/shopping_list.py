from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import ShoppingList, UserListItem, UserItem

def get_shopping_list(user_id):
    return ShoppingList.objects.get(fk=user_id)

def get_user_list_items(shopping_list_id):
    return UserListItem.objects.get(shopping_list_id)

def get_user_items(item_id):
    return UserItem.objects.get(item_id)


@login_required
def shopping_list(request, user_id):
    user_shopping_list = get_shopping_list(user_id)
    