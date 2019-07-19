# titlegen.py
# Light Novel Title Generator
# Init 11-14-18
# WulfOrc

import itertools

import random

#Title Arrays - - - One of each of these options will be chosen, in order, to make a full title
zeroth = ['My', 'My Girlfriend\'s ', 'My Teacher\'s', 'My Senpai\'s', 'My Boss\'s', 'My Best Friend\'s']

first = ['Sister', 'Step Sister', 'Brother', 'Kid Brother', 'Cat', 'Dog', 'Step Dog', 'Mother',
         'Father', 'Kid Sister', 'Twin Sister', 'Twin Brother', 'Step Father', 'Cute Neighbor',
         'Ghost of my Grandmother', 'Sandwich', 'Demon', 'Grandmother', 'Butler']

second = ['is','was']

third = ['', 'turned into', 'forced to be', 'asking me to be', 'reincarnated as']

fourth = ['a washing machine', 'my coworker', 'a cannibal','a family pet', 'a demon', 'an angel',
         'a secret agent', 'a spy', 'a dungeon gremlin', 'a guild leader', 'an MMO healslut',
         'a real-life furry', 'a Silicon Valley tech bro', 'a computer program', 'a cat', 'a Vocaloid', 'a mad scientist', 'a slime girl', 
         ' a monster-girl', 'a monster-boy', 'my bara fantasy', 'your anime crush', 'my waifu', 'your waifu', 'an incel', 'a neckbeard', 
         'a member of the Real Housewives', 'an Orc', 'a Furry', 'a Mastodon Instance Admin', 'a DM', 'a celebrity', 'a cam model' ]

fourthcomma = [',']

fifth = ['and now I', 'but I', 'and we']

sixth = ['have to smell feet all day', 'have to eat alongside them', 'have to live a real-life romcom',
         'have to explore the local dungeon', 'have to be surrounded by NERDS', 'Don\'t think this will end well']

seventh = ['', '?', '?!', '!']

titles = []

#Generate combos to add to titles
def gen_titles():
    print('The Name of Your New Serial Light Novel Is:')

    for title in itertools.product(zeroth, first, second, third, fourth, fourthcomma, fifth, sixth, seventh) :
        titles.append(title)

#Show title list
def show_titles() :
    finaltitle = [random.choice(titles)]
    for t in finaltitle:
        print(' '.join(t))
#run combos
gen_titles()

#run list
show_titles()