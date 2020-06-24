from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import UserItem, Item, Location, Category, Store
import datetime

import time

@login_required
def user_item_list(request):
    if request.method == 'GET':
        all_items = UserItem.objects.filter(user_id=request.user.id).exclude(quantity=0)
        zero_items = UserItem.objects.filter(user_id=request.user.id, quantity=0)

        for user_item in all_items:
            user_item.Item = Item.objects.filter(id=user_item.item_id)

        for zero_item in zero_items:
            # try:
            zero_item.Item = Item.objects.filter(id=zero_item.item_id)
            # except:
            #     pass
        template = 'items/item_list.html'
        context = {
            'all_items': all_items,
            'zero_items': zero_items
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if "new_item" in form_data and form_data["new_item"] == "True":

            new_item = Item.objects.create(
                name=form_data['name'],
                description=form_data['description'],
                image="data:image/jpeg;base64,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",

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
