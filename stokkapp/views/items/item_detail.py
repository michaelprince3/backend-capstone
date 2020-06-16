from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import UserItem

def get_user_item(user_item_id):
    return UserItem.objects.get(pk=user_item_id)

@login_required
def user_item_details(request, user_item_id):
    user_item = get_user_item(user_item_id)
    if request.method == 'GET':
        
        template = 'items/item_details.html'
        context = {
            'user_item': user_item
        }
        
        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST
        
        if (
            "actual method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            
            user_item.delete()
            
            return redirect(reverse('stokkapp:home'))

