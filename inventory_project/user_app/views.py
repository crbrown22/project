from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user_name=form.cleaned_data.get('username')
            messages.success(request, f'{user_name} has been registered')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    
    context = {
        'form':form
    }
    return render(request, 'user/register.html', context)

@login_required(login_url='user-login')
def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            user_name=user_form.cleaned_data.get('username')
            messages.success(request, f'{user_name} has been updated')
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance= request.user.profile)
    context={
            'user_form':user_form,
            'profile_form':profile_form

    }
    return render(request, 'user/profile_update.html', context)

#def login(request):
    #return render(request, 'user/login.html')

#def logout(request):
    #return render(request, 'user/logout.html')