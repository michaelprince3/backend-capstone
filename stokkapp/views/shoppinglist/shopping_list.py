from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import ShoppingList, UserListItem, UserItem


def get_user_list_items(new_user_id):
    return UserItem.objects.filter(user_id=new_user_id, quantity=0)


# def shopping_list_item(request, user_item):
#     if request.method == 'GET':
#         new_user_id = request.user.id
#         user_shopping_list = ShoppingList.objects.get(user_id=new_user_id)

#         new_list_item = UserListItem.objects.create(
#             shopping_list_id=user_shopping_list.id,
#             item_id=user_item
#         )

#         return redirect(reverse('stokkapp:detail', args=[user_item]))


@login_required
def shopping_list(request):
    if request.method == 'GET':
        name=request.user.username
        new_user_id = request.user.id
        all_user_items = get_user_list_items(new_user_id)
        
        # try:
        #     user_shopping_list = ShoppingList.objects.get(user_id=new_user_id)
        #     print(user_shopping_list.id)
        # except:
        #     user_shopping_list = ShoppingList.objects.create(
        #         name=request.user.username,
        #         user_id=new_user_id
        #     )

        # try:
        #     user_list_items = get_user_list_items(user_shopping_list.id)

        #     for user_list_item in user_list_items:
        #         user_list_item.item = UserItem.objects.filter(
        #             id=user_list_item.item_id)
                
        # except:
        #     # user_shopping_list = ShoppingList.objects.get(user_id=new_user_id)
        #     # user_list_items = UserListItem.objects.create(
        #     #     shopping_list_id=user_shopping_list.id,
        #     #     item_id="1"
        #     # )

        template = 'shoppinglist/shopping_list.html'
        context = {
            'name': name,
            'user_list_items': all_user_items
        }

        return render(request, template, context)
