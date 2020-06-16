from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import UserItem, Item, Location, Category, Store
import datetime

def user_item_list(request):
    if request.method == 'GET':
        all_items = UserItem.objects.all()
        
        for user_item in all_items:
            user_item.Item = Item.objects.filter(id = user_item.item_id)
        
        template = 'items/item_list.html'
        context = {
            'all_items': all_items
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        new_User_item = UserItem.objects.create(
            size = form_data['size'],
            quantity = form_data['quantity'],
            expiration = form_data['expiration'],
            purchase_date = datetime.datetime.now,
            category_id = form_data['category'],
            item_id = form_data['item'],
            location_id = form_data['location'],
            store_id = form_data['store'],
            user_id = request.user.id
        )
        
        return redirect(reverse('stokkapp:user_item_list'))