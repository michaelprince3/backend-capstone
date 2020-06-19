from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import UserItem


def get_user_item(user_item_id):
    return UserItem.objects.get(pk=user_item_id)


@login_required
def user_item_details(request, user_item_id):
    user_item = get_user_item(user_item_id)
    if request.method == 'GET':

        template = 'items/item_detail.html'
        context = {
            'user_item': user_item
        }

        return render(request, template, context)

    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):

            user_item.delete()

            return redirect(reverse('stokkapp:user_item_list'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            user_item.size = form_data['size']
            user_item.quantity = form_data['quantity']
            user_item.expiration = form_data['expiration']
            user_item.category_id = form_data['category']
            user_item.item_id = form_data['item']
            user_item.location_id = form_data['location']
            user_item.store_id = form_data['store']

            user_item.save()

            return redirect(reverse('stokkapp:detail', args=[user_item.id]))
