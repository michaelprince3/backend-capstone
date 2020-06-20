from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from stokkapp.models import Location
import datetime

import time


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