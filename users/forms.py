from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Password

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email')

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ('current_password',
                  'new_password',
                  'new_password_confirmation')
