from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, UpdateUserForm, UpdateProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.db import transaction
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

#ACCOUNT
@login_required
def account_detail(request, account_username):
    user = User.objects.get(username=account_username)
    return render(request, 'account_detail.html', {'user': user})

@login_required
def account_update(request, account_username):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your account was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'account_update.html', { 'form': form })



#PROFILES
def profile_detail(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    return render(request, 'profile_detail.html', {'profile':profile})


@login_required
def profile_update(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail', profile_pk=profile_pk)
    else:
        form = UpdateProfileForm()
    return render(request, 'profile_update.html', {'profile':profile, 'form':form})















#joining 2 forms in a view example:
# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         update_user_form = UpdateUserForm(request.POST, instance=request.user)
#         update_profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
#         if update_user_form.is_valid() and update_profile_form.is_valid():
#             update_user_form.save()
#             update_profile_form.save()
#             messages.success(request, ('Your profile was successfully updated!'))
#             return redirect('home')
#         else:
#             messages.error(request, ('Please correct the error below.'))
#     else:
#         update_user_form = UpdateUserForm(instance=request.user)
#         update_profile_form = UpdateProfileForm(instance=request.user.profile)
#     return render(request, 'account_update.html', {
#         'update_user_form': update_user_form,
#         'update_profile_form': update_profile_form
#     })
