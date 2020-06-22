from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import Store


@login_required
def store_list(request):
    if request.method == 'GET':
        all_stores = Store.objects.all()

        template = 'store/store_list.html'
        context = {
            'all_stores': all_stores,

        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        

        new_store = Store.objects.create(
            name=form_data['name'],

        )
        
        return redirect(reverse('stokkapp:stores'))

@login_required
def store_modify(request, store_id):
    all_stores = Store.objects.all()
    one_store = Store.objects.get(pk=store_id)
    if request.method == 'GET':
    
        template = 'store/store_list.html'
        context = {
            'all_stores': all_stores,
            'one_store': one_store

        }

        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            one_store.name = form_data['name']
            
            one_store.save()
            
            return redirect(reverse('stokkapp:stores'))
        
        if ( 
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):
            
            one_store.delete()
            
            return redirect(reverse('stokkapp:stores'))