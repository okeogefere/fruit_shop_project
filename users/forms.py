from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import *

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':"w-100 form-control border-0 py-3 mb-4", 'placeholder': 'Full Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':"w-100 form-control border-0 py-3 mb-4", 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"w-100 form-control border-0 py-3 mb-4", 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"w-100 form-control border-0 py-3 mb-4", 'placeholder': 'Confirm Password'})) 
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2']
