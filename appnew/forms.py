from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['name','email','password']

class login_form(forms.Form):
    email=forms.EmailField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())

