from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import CustomUser
from django.core.exceptions import ValidationError



def validate_gmail(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('Email address must end with @gmail.com')

class LoginForm(AuthenticationForm):
    username = forms.EmailField() #validators=[validate_email, validate_gmail]
    password = forms.PasswordInput()
    
