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
        path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
        path('category/<slug:category_name_slug>/<slug:game_name_slug>', views.show_game, name='show_game'),
        ]