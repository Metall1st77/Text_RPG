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

from main import main
from field import field
from fight import fight

if __name__ == "__main__":
    game = main()
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

    fight = fight(man.portrait)
