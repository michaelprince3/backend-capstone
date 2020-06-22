from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import Category


@login_required
def category_list(request):
    if request.method == 'GET':
        all_categories = Category.objects.all()

        template = 'category/category_list.html'
        context = {
            'all_categories': all_categories,

        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        

        new_category = Category.objects.create(
            name=form_data['name'],

        )
        
        return redirect(reverse('stokkapp:categories'))

@login_required
def category_modify(request, category_id):
    all_categories = Category.objects.all()
    one_category = Category.objects.get(pk=category_id)
    if request.method == 'GET':
    
        template = 'category/category_list.html'
        context = {
            'all_categories': all_categories,
            'one_category': one_category

        }

        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            one_category.name = form_data['name']
            
            one_category.save()
            
            return redirect(reverse('stokkapp:categories'))
        
        if ( 
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):
            
            one_category.delete()
            
            return redirect(reverse('stokkapp:categories'))