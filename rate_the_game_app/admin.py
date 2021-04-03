from django.contrib import admin
from rate_the_game_app.models import UserProfile, Category, Game, Review

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Game)
admin.site.register(Review)
