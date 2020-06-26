from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import UserItem, Item, Location, Category, Store
import datetime

import time

@login_required
def user_item_list(request):
    if request.method == 'GET':
        all_items = UserItem.objects.filter(user_id=request.user.id).exclude(quantity=0)
        zero_items = UserItem.objects.filter(user_id=request.user.id, quantity=0).exclude(expiration__lte=datetime.datetime.now())
        exp_items = UserItem.objects.filter(user_id=request.user.id, expiration__lte=datetime.datetime.now())

        for user_item in all_items:
            user_item.Item = Item.objects.filter(id=user_item.item_id)

        for zero_item in zero_items:
            zero_item.Item = Item.objects.filter(id=zero_item.item_id)
            
        for exp_item in exp_items:
            exp_item.Item =Item.objects.filter(id=exp_item.item_id)

        template = 'items/item_list.html'
        context = {
            'all_items': all_items,
            'zero_items': zero_items,
            'exp_items': exp_items
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if "new_item" in form_data and form_data["new_item"] == "True":

            new_item = Item.objects.create(
                name=form_data['name'],
                description=form_data['description'],
                image="image/foodImage.jpeg",

            )

            new_User_item = UserItem.objects.create(
                size=form_data['size'],
                quantity=form_data['quantity'],
                expiration=form_data['expiration'],
                purchase_date=datetime.datetime.now,
                category_id=form_data['category'],
                item_id=new_item.id,
                location_id=form_data['location'],
                store_id=form_data['store'],
                user_id=request.user.id
            )

        else:
            new_User_item = UserItem.objects.create(
                size=form_data['size'],
                quantity=form_data['quantity'],
                expiration=form_data['expiration'],
                purchase_date=datetime.datetime.now,
                category_id=form_data['category'],
                item_id=form_data['item'],
                location_id=form_data['location'],
                store_id=form_data['store'],
                user_id=request.user.id
            )

        return redirect(reverse('stokkapp:user_item_list'))
