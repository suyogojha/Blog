from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    pass

class CustomUserSignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username", "email", "password", "password1")
        
    