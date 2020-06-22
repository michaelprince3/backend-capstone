from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import Location

@login_required
def location_list(request):
    if request.method == 'GET':
        all_locations = Location.objects.all()

        template = 'location/location_list.html'
        context = {
            'all_locations': all_locations,

        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        

        new_location = Location.objects.create(
            name=form_data['name'],

        )
        
        return redirect(reverse('stokkapp:locations'))

@login_required
def location_modify(request, location_id):
    all_locations = Location.objects.all()
    one_location = Location.objects.get(pk=location_id)
    if request.method == 'GET':
    
        template = 'location/location_list.html'
        context = {
            'all_locations': all_locations,
            'one_location': one_location

        }

        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            one_location.name = form_data['name']
            
            one_location.save()
            
            return redirect(reverse('stokkapp:locations'))
        
        if ( 
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):
            
            one_location.delete()
            
            return redirect(reverse('stokkapp:locations'))