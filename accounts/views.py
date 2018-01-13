from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, UpdateUserForm, UpdateProfileForm

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



@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        update_user_form = UpdateUserForm(request.POST, instance=request.user)
        update_profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if update_user_form.is_valid() and update_profile_form.is_valid():
            update_user_form.save()
            update_profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        update_user_form = UpdateUserForm(instance=request.user)
        update_profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'my_account.html', {
        'update_user_form': update_user_form,
        'update_profile_form': update_profile_form
    })


