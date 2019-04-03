import random
import sys
import math

import human
import werewolf
import treant
import tech
import demon

max_level  = 100
max_attack = 100
max_health = 100
max_armor = 100

sexes = ('male', 'female')
male_names = ('Avraam', 'Ben', 'Carl', 'Dennis', 'Eagle', 'Franc')
female_names = ('Alivia', 'Bella', 'Clara', 'Danna', 'Erica', 'Felicia')
jobs = ('none', 'quest', 'helper', 'warrior')
races = ('human', 'werewolf', 'treant', 'tech', 'demon')
dangers = ('none', 'unknown', 'safe', 'unstable', 'dangerous')

job_for_race = {'human' : 'trader',
                'werewolf' : 'hunter',
                'treant' : 'forester',
                'tech' : 'engineer',
                'demon' : 'devourer'}

interferences = ('@', '#', '$', '%', '&', '*')

if __name__ == "__main__":
    # creating a mob needs (sex, level, danger lvl, attack, health, armor, job)
    sex = 'male'
    race = 'human'
    level = 1
    danger = 'none'
    attack = 30
    health = 100
    armor = 30
    job = 'none'

    mob = creature(sex, race, level, danger, attack, health, armor, job)
    mob.set_name('George', True)
    mob.levelup(True)
    mob.set_job('helper', True)

    print()

    man = human(sex, race, level, danger, attack, health, armor, job)
    man.levelup(True)
    man.print_stats()
