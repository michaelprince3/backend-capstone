from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect(reverse('stokkapp:home'))

    else:
        f = UserCreationForm()

    template = 'registration/register.html'
    context = {
        'form': f
    }

    return render(request, template, context)
