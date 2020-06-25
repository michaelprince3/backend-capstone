from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import UserItem, Store
import datetime


def get_user_list_items(new_user_id):
    return UserItem.objects.filter(user_id=new_user_id)


def get_stores():
    return Store.objects.all


@login_required
def shopping_list(request):
    if request.method == 'GET':
        name = request.user.username
        new_user_id = request.user.id
        all_user_items = get_user_list_items(new_user_id)
        zero_items = all_user_items.filter(quantity=0).exclude(expiration__lte=datetime.datetime.now())
        exp_items = all_user_items.filter(
            expiration__lte=datetime.datetime.now())

        template = 'shoppinglist/shopping_list.html'
        context = {
            'name': name,
            'user_list_items': zero_items,
            'exp_items': exp_items
        }

        return render(request, template, context)


@login_required
def shopping_list_store(request):
    if request.method == 'GET':
        name = request.user.username
        new_user_id = request.user.id
        all_user_items = get_user_list_items(new_user_id)
        zero_items = all_user_items.filter(quantity=0).exclude(expiration__lte=datetime.datetime.now())
        exp_items = all_user_items.filter(
            expiration__lte=datetime.datetime.now())
        all_stores = get_stores()

        # for store in all_stores:
        #     store.user_items = zero_items.filter(store_id=store.id)

        template = 'shoppinglist/shopping_list_stores.html'
        context = {
            'name': name,
            'stores': all_stores,
            'user_list_items': zero_items,
            'exp_items': exp_items
            
        }

        return render(request, template, context)
