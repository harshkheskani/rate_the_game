# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:37:29 2021

@author: Harvey
"""
from django import forms
from rate_the_game_app.models import UserProfile, Game, Review, Category
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
    
class GameForm(forms.ModelForm):
    title = forms.CharField(max_length=Game.TITLE_MAX_LENGTH, help_text="Please enter the name of the game.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    # category information is already passed via the view so is not required in the form
    class Meta:
        model = Game
        exclude = ('category',)
        
class ReviewForm(forms.ModelForm):
    score = forms.IntegerField(help_text="Please enter a score between 1 and 10 for this game.")
    comment = forms.CharField(max_length=Review.REVIEW_MAX_LENGTH,widget=forms.Textarea,help_text="Please leave a comment to finish your review")
    # username and game title information is already passed via the view so is not required in the form
    class Meta:
        model = Review
        exclude = ('user','game',)
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(ReviewForm, self).__init__(*args, **kwargs)
