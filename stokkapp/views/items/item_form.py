from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from stokkapp.models import UserItem, Item, Location, Category, Store
from .item_detail import get_user_item


def get_user_item(user_item_id):
    return UserItem.objects.get(pk=user_item_id)


def get_items():
    return Item.objects.all()


def get_locations():
    return Location.objects.all()


def get_categories():
    return Category.objects.all()


def get_stores():
    return Store.objects.all()


@login_required
def user_item_form(request):
    if request.method == 'GET':
        items = get_items()
        locations = get_locations()
        categories = get_categories()
        stores = get_stores()

        template = 'items/item_form.html'
        context = {
            'all_items': items,
            'all_locations': locations,
            'all_categories': categories,
            'all_stores': stores
        }

        return render(request, template, context)


@login_required
def new_user_item_form(request):
    if request.method == 'GET':
        locations = get_locations()
        categories = get_categories()
        stores = get_stores()

        template = 'items/item_form.html'
        context = {
            'all_locations': locations,
            'all_categories': categories,
            'all_stores': stores
        }

        return render(request, template, context)


@login_required
def user_item_edit_form(request, user_item_id):
    if request.method == 'GET':
        user_item = get_user_item(user_item_id)
        items = get_items()
        locations = get_locations()
        categories = get_categories()
        stores = get_stores()

        template = 'items/item_form.html'
        context = {
            'user_item': user_item,
            'all_items': items,
            'all_locations': locations,
            'all_categories': categories,
            'all_stores': stores
        }

        return render(request, template, context)
