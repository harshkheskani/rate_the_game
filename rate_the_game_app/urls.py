# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:47:37 2021

@author: Harvey
"""

from django.urls import path
from rate_the_game_app import views

app_name = 'rate_the_game_app'

urlpatterns = [
        path('register/', views.register, name='register'),
        path('login/', views.user_login, name='login'),
        path('logout/', views.user_logout, name='logout'),
        path('my_account/', views.my_account, name='my_account')
        ]