# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:37:29 2021

@author: Harvey
"""
from django import forms
from rate_the_game_app.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
 
       
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('picture',)

# class Contact(forms.Form):
#     first_name = forms.CharField(max_length = 50)
#     last_name = forms.CharField(max_length = 50)
#     email_address = forms.EmailField(max_length = 150)
#     message = forms.CharField(widget = forms.Textarea, max_length = 2000)
def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=80)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])
    