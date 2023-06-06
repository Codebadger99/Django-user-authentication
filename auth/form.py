from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'type': 'text',
        'id': 'username'
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'type':'email',
    }))
     
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'type':'password',
        'id': 'password'
    }))
      
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Confirm Password',
        'type':'password',
        'id': 'password'
    }))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
