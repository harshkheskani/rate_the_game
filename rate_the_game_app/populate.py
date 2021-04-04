import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rate_the_game.settings')

import django
django.setup()

from rate_the_game_app.models import Category, Game, Review

def populate():
    action = [
        {'title':'Tekken 3', 'user':'harvey2001', 'score':'7.5/10', 'comment':'A lot of fun would reccommend'},
        {'title':'Farcry 5', 'user':'ricky2051', 'score':'7/10', 'comment':'Amazing story!'},
        {'title':'Super Mario Galaxy', 'user':'harsh2801', 'score':'4/10', 'comment':'Had a blast while playing!'},
        {'title':'Super Smash Bros Brawl', 'user':'UofG2019', 'score':'9/10', 'comment':'Got super heated when playing with friends'},
        {'title':'Half-Life 2', 'user':'WAD2510', 'score':'5/10', 'comment':'It was alright, quite repetitative'},
    ]
    adventure = [
        {'title':'The Last Of Us', 'user':'WAD2510', 'score':'10/10', 'comment':'It was extremely immersive, and beautiful story'},
        {'title':'Super Mario World', 'user':'ricky2051', 'score':'8.5/10', 'comment':'Made me feel nostalgic, still as same as I remeber it!'},
        {'title':'Pokemon: Diamond and Pearl', 'user':'harsh2801', 'score':'9.5/10', 'comment':'So much fun, would wish for it to be longer'},
        {'title':'Zelda: Breath of the Wild', 'user':'UofG2019', 'score':'8/10', 'comment':'Beautiful visuals'},
        {'title':'Cyberpunk 2077', 'user':'harvey2001', 'score':'6.5/10', 'comment':'So much potential, but fell a little short!'},
    ]
    casual = [
        {'title':'Minecraft', 'user':'harvey2001', 'score':'7.5/10', 'comment':'A classic!'},
        {'title':'Stardew Valley', 'user':'ricky2051', 'score':'9/10', 'comment':'Something very relaxing about it'},
        {'title':'Portal 2', 'user':'harsh2801', 'score':'8/10', 'comment':'After 7 years so much fun'},
        {'title':'Terreria', 'user':'WAD2510', 'score':'7/10', 'comment':'Not as func as minecraft but hey'},
        {'title':'Rocket League', 'user':'UofG2019', 'score':'10/10', 'comment':'Insanity!'},
    ]
    indie = [
        {'title':'Cuphead', 'user':'UofG2019', 'score':'7.5/10', 'comment':'Great graphics but super difficult'},
        {'title':'Super Meat Boy', 'user':'ricky2051', 'score':'6/10', 'comment':'Way too short! but still fun'},
        {'title':'Rust', 'user':'harsh2801', 'score':'8/10', 'comment':'So much  fun with friends'},
        {'title':'Overcooked 2', 'user':'harvey2001', 'score':'5/10', 'comment':'Fun but repetative'},
        {'title':'Totally Accurate Battle Simulator', 'user':'WAD2510', 'score':'8.5/10', 'comment':'It great new take on the indie genre!'},

    ]

    massively_multiplayer = [
        {'title':'Battlefield 3', 'user':'harvey2001', 'score':'7.5/10', 'comment':'Bautiful!'},
        {'title':'Among Us', 'user':'ricky2051', 'score':'8.5/10', 'comment':'ave to lie to my friends but still fun!'},
        {'title':'Fall Guys', 'user':'harsh2801', 'score':'4.5/10', 'comment':'Got boring fast!'},
        {'title':'Fortnite', 'user':'WAD2510', 'score':'8/10', 'comment':'A really creative game, but hard to learn'},
        {'title':'Valorant', 'user':'UofG2019', 'score':'8/10', 'comment':'A mix between CS:GO and overwatch'},
    ]

    racing = [
        {'title':'Need for Speed: Most Wanted', 'user':'harvey2001', 'score':'10/10', 'comment':'Forever classic'},
        {'title':'Mario Kart', 'user':'ricky2051', 'score':'10/10', 'comment':'GOAT'},
        {'title':'Forza Horizon', 'user':'harsh2801', 'score':'7/10', 'comment':'Amzing vizuals'},
        {'title':'Trackmania', 'user':'UofG2019', 'score':'7/10', 'comment':'Throwback!'},
        {'title':'Gran Turismo 5', 'user':'WAD2510', 'score':'4/10', 'comment':'Quite oring, feels limited for a racing game'},
    ]

    rpg = [
        {'title':'Dark Souls', 'user':'UofG2019', 'score':'7/10', 'comment':'Really engaging, but quite dark'},
        {'title':'The Elder Scrolls V: Skyrim', 'user':'ricky2051', 'score':'9.5/10', 'comment':'Intense as hell'},
        {'title':'The Witcher 3: Wild Hunt', 'user':'harsh2801', 'score':'10/10', 'comment':'Stunning game, amazing story'},
        {'title':'Fallout 4', 'user':'WAD2510', 'score':'6/10', 'comment':'Was hopinng for more but still fun'},
        {'title':'South Park: The Stick of Truth', 'user':'harvey2001', 'score':'8.5/10', 'comment':'Way too funny!'},
    ]

    simulation = [
        {'title':'Kerbal Space Program', 'user':'harvey2001', 'score':'5.5/10', 'comment':'Extremely interesting'},
        {'title':'Euro Truck Simulator 2', 'user':'ricky2051', 'score':'5/10', 'comment':'Really realistic'},
        {'title':'Planet Coaster', 'user':'WAD2510', 'score':'7/10', 'comment':'Such a goofy game'},
        {'title':'The Sims 4', 'user':'UofG2019', 'score':'8.5/10', 'comment':'Classic!'},
        {'title':'Microsoft Flight Simulator', 'user':'harsh2801', 'score':'9.5/10', 'comment':'Insanely immersive, super realistic'},
    ]

    sports = [
        {'title':'FIFA 21', 'user':'harsh2801', 'score':'7.5/10', 'comment':'Would like something newer but still classic fifa'},
        {'title':'NBA2K21', 'user':'UofG2019', 'score':'9/10', 'comment':'MyCarrear was amazing!'},
        {'title':"Tony Hawk's Pro Skater 1 + 2", 'user':'ricky2051', 'score':'8.5/10', 'comment':'It beena while, but worth the wait'},
        {'title':'Madden NFL 21', 'user':'harvey2001', 'score':'7/10', 'comment':'Hmm its the same every year, but still fun'},
        {'title':'NFL2K21', 'user':'WAD2510', 'score':'7/10', 'comment':'New player designs are amazing'},
    ]

    strategy = [
        {'title':'Civilization VI', 'user':'harsh2801', 'score':'9.5/10', 'comment':'The possibilities are endless'},
        {'title':'Plague Inc.', 'user':'WAD2510', 'score':'7.5/10', 'comment':'Every game is unique'},
        {'title':'Evil Genius 2: World Domination', 'user':'UofG2019', 'score':'8.5/10', 'comment':'So much fun!'},
        {'title':'Stellaris', 'user':'ricky2051', 'score':'8/10', 'comment':'Love the sci-fi vibe'},
        {'title':'XCOM 2', 'user':'harvey2001', 'score':'8.5/10', 'comment':'Really unique take on a strategy game'},
    ]

    games = {'Action': {'games':action},
             'Adventure': {'games':adventure},
             'Casual': {'games':casual},
             'indie':{'games':indie},
             'massively_multiplayer':{'games':massively_multiplayer},
             'racing':{'games':racing},
             'rpg':{'games':rpg},
             'simulation':{'games':simulation},
             'sports':{'games':sports},
             'strategy':{'games':strategy},
             }

    for cat, cat_data in categories.items():
        c = add_cat(cat)
        for q in cat_data["games"]:
            add_game(c, q["title"], q["user"], q["score"], q["comment"])
    
    for c in Category.objects.all():
        for q in Game.objects.filter(category=c):
            print(f"- {c}: {q}")
    
    def add_game (cat, title, user, score, comment):
        q = Game.objects.get_or_create(category=cat, game=title)
        q.user=user
        q.score=score
        q.comment=comment
    
    def add_cat(name):
        c=Category.objects.get_or_create(name=name)[0]
        c.save()
        return c
    if __name__="__main__":
        print("Starting RTG population")
        populate()