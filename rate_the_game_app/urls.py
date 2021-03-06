# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 12:47:37 2021

@author: Harvey
"""

from django.urls import path
from rate_the_game_app import views

app_name = 'rate_the_game_app'

urlpatterns = [
        path('', views.index, name='index'),
        path('index/', views.index, name = 'index_page'),
        path('register/', views.register, name='register'),
        path('login/', views.user_login, name='login'),
        path('category/', views.show_list, name='show_list'),
        path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
        path('category/<slug:category_name_slug>/add_game/', views.add_game, name='add_game'),
        path('category/<slug:category_name_slug>/<slug:game_name_slug>/', views.show_game, name='show_game'),
        path('category/<slug:category_name_slug>/<slug:game_name_slug>/add_review/', views.add_review, name='add_review'),
        path('logout/', views.user_logout, name='logout'),
        path('my_account/', views.my_account, name='my_account'),
        path('contact/', views.contact_form, name='contact'),
        ]
