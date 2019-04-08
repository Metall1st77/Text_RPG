import random
import sys
import math
import time

from creature import creature
from human import human
from werewolf import werewolf
from treant import treant
from tech import tech
from demon import demon

import main

max_level  = 100
max_attack = 100
max_health = 100
max_armor = 100

job_for_race = {'human' : 'trader',
                'werewolf' : 'hunter',
                'treant' : 'forester',
                'tech' : 'engineer',
                'demon' : 'devourer'}

interferences = ('@', '#', '№', '$', '%', '&', '*')

if __name__ == "__main__":
    main.menu(True)
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
    mob.set_name('fFfFFfFeeEge', True)
    mob.levelup(True)
    mob.set_job('helper', True)

    print()

    man = human(sex, race, level, danger, attack, health, armor, job)
    man.levelup(True)
    man.print_stats()
