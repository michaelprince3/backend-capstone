from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import ShoppingList, UserListItem, UserItem


def get_user_list_items(shopping_list_id):
    return UserListItem.objects.filter(shopping_list_id = shopping_list_id)

def shopping_list_item(request, user_item):
    if request.method == 'GET':
        new_user_id = request.user.id
        user_shopping_list = ShoppingList.objects.get(user_id = new_user_id)
        
        new_list_item = UserListItem.objects.create(
            shopping_list_id=user_shopping_list.id,
            item_id=user_item
        )
        
        return redirect(reverse('stokkapp:detail', args=[user_item]))

@login_required
def shopping_list(request):
    if request.method == 'GET':
        new_user_id = request.user.id
        print(new_user_id)

        try:
            user_shopping_list = ShoppingList.objects.get(user_id = new_user_id)
            print(user_shopping_list.id)
        except:
            user_shopping_list = ShoppingList.objects.create(
                name=request.user.username,
                user_id=new_user_id
            )


        try:
            user_list_items = get_user_list_items(user_shopping_list.id)

            for user_list_item in user_list_items:
                user_list_item.item = UserItem.objects.filter(
                    id=user_list_item.item_id)
        except:
            pass
            # return('There are no items in your list')

        
            template = 'shoppinglist/shopping_list.html'
            context = {
                'user_shopping_list': user_shopping_list,
                'user_list_items': user_list_items
            }

            return render(request, template, context)
