import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_the_game_app.settings')

import django
django.setup()

from rate_the_game_app.models import Category, Game, Review

def populate():
    action = [
        {'title':'Tekken 3', 'user':'harvey2001', 'score':'7.5/10', 'comment':'A lot of fun would reccommend'},
        {'title':'Tekken 4', 'user':'harvey2001', 'score':'8.5/10', 'comment':'A lot of fun would reccommend'}
    ]
    adventure = [
        {'title':'Tekken 4', 'user':'harvey2001', 'score':'8.5/10', 'comment':'A lot of fun would reccommend'}
    ]
    casual = [
        {'title':'Tekken 5', 'user':'harvey2101', 'score':'7/10', 'comment':'A lot of fun would reccommend'}
    ]
    games = {'Action': {'games':action},
             'Adventure': {'games':adventure},
             'Casual': {'games':casual},}

    for game, game_data in games.items():
        g = add_game(game)
        for game in game_data['games']:
            add_game(g, game['title'], game['user'],game['score'], game['comment'])

    for c in Category.object.all():
        for g in Game.object.all(category=c):
            print (f'- {c}:{g}')

