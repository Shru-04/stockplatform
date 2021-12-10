from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)
    email = forms.CharField(widget=forms.EmailInput,required=False)
    first_name = forms.CharField(max_length=200,required=False)
    last_name = forms.CharField(max_length=200,required=False)
    