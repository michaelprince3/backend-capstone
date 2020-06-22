from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import ShoppingList, UserListItem, UserItem

def get_user_item(user_item_id):
    return UserItem.objects.get(pk=user_item_id)

def shopping_list_item(request, user_item_id):
    user_item = get_user_item(user_item_id)
    if request.method == 'GET':
        new_user_id = request.user.id
        user_shopping_list = ShoppingList.objects.get(user_id=new_user_id)

        new_list_item = UserListItem.objects.create(
            shopping_list_id=user_shopping_list.id,
            item_id=user_item_id
        )

        return redirect(reverse('stokkapp:detail', args=[user_item_id]))

    if request.method == 'POST':
        form_data = request.POST
        if (
                "actual_method" in form_data
                and form_data["actual_method"] == "PUT"
            ):
                print(form_data['quantity'])
                user_item.quantity = form_data['quantity']

                user_item.save()

                return redirect(reverse('stokkapp:detail', args=[user_item_id]))  
