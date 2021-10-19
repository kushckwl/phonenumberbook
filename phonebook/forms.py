from django import forms
from django.contrib.auth import models
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
        class Meta:
            model = Contact
            fields = ['id','name','number','date_added']

class SignupForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput()) 
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')           