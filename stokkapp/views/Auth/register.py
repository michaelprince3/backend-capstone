from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms import ValidationError


def register (request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('')
        
    else:
        f = UserCreationForm()
        
    template = 'registration/register.html'
        
    return render(request, template, {'form': f})
    
# def register(request):
#     if request.method == 'POST':
#         form_data = request.POST
        
#         try:
#             if form_data['password'] != form_data['password_confirmation']:
#                 raise ValidationError("Password and password confirmation do not match.")
              
#             new_user = User.objects.create_user(
#                 username=form_data['username'],
#                 password=form_data['password']
#             )

#             new_user.librarian.location_id=form_data['location']
#             new_user.librarian.save()
            
#             user = authenticate(request, username=form_data['username'], password=form_data['password'])
#             if user is not None:
#                 login(request, user)
#                 # Redirect to a success page.
#                 return redirect(reverse('stokkapp:home'))
#         except Exception as e:
#             messages.error(request, f'{type(e)}: {e}')
          
                

#     libraries = Library.objects.all()
#     template = 'registration/register.html'
#     context = {
#         'libraries': libraries
#     }

#     return render(request, template, context)