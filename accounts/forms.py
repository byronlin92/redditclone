from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from forums.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email']

#
# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio']



