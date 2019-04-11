import random
import sys
import math
import time
import re

from creature import creature
from human import human
from werewolf import werewolf
from treant import treant
from tech import tech
from demon import demon

from field import field
from fight import fight

class main:
    progress = 0
    max_progress = 10
    # TODO: commands
    directions = ( ('left',  'a'),
                   ('right', 'd'),
                   ('up',    'w'),
                   ('down',  's') )

    items = ( 'sword',
              'knife' )

    commands = { 'menu'     : ('continue', 'new', 'load'),
                 'pause'    : ('continue', 'restart', 'save', 'load'),
                 'fight'    : ('attack', 'defend', 'retire', 'payoff'),
                 'walk'     : (('go', directions), ('move', directions)),
                 'shop'     : (('buy', items), ('sell', items)),
                 'anywhere' : ('pause', 'quit') }

    def __init__(self):
        # TODO: init function
        self.menu(True)
        return

    def clear_screen(self):
        for i in range(0, 50):
            print("\n")

    # def loading(t = 1):
    #     # clear_screen()
    #     k = 0
    #     print("Loading", end='')
    #     while k < 3:
    #         time.sleep(1)
    #         print(".", end='')
    #         k += 1


    def command(self, status = 'menu'):
        # status may have values: 'menu', 'pause', 'fight', 'walk', 'shop'
        cmd = input()
        cmd = re.sub(r'\s', ' ', cmd.lower())
        cmd = cmd.split()
        while not cmd[0] in commands[status]:
            print("Wrong command. Type 'info' to see what you can do.\n")
            cmd = input()
            cmd = re.sub(r'\s', ' ', cmd.lower())
            cmd = cmd.split()
        # TODO:

    def attack(self):
        # TODO: attack function
        return

    def defend(self):
        # TODO: defend function
        return

    def move(self, direction):
        # TODO: move function
        return

    def create_character(self):
        level = 0
        danger = job = None
        attack = health = 100
        armor = 50

        race = input("Choose your race (human, werewolf, tech, treant, demon. Type 'info' to see information about races): ")
        race = re.sub(r'\s', '', race.lower())
        while not race in creature.races:
            if race == 'info':
                self.clear_screen()
                print('\n{:*^30}'.format(' HUMAN '))
                human.info()
                print('\n{:*^30}'.format(' WEREWOLF '))
                werewolf.info()
                print('\n{:*^30}'.format(' TECH '))
                tech.info()
                print('\n{:*^30}'.format(' TREANT '))
                treant.info()
                print('\n{:*^30}'.format(' DEMON '))
                demon.info()
            print("Type correct race or 'info', please.")
            race = input()
            race = re.sub(r'\s', '', race.lower())


        sex = input("Choose your sex (male, female): ")
        sex = re.sub(r'\s', '', sex.lower())
        while not sex in creature.sexes:
            print("Type correct sex, please.")
            sex = input()
            sex = re.sub(r'\s', '', sex.lower())

        if race == 'human':
            character = human(sex, race, level, danger, attack, health, armor, job)
        elif race == 'demon':
            character = demon(sex, race, level, danger, attack, health, armor, job)
        elif race == 'tech':
            character = tech(sex, race, level, danger, attack, health, armor, job)
        elif race == 'treant':
            character = treant(sex, race, level, danger, attack, health, armor, job)
        elif race == 'werewolf':
            character = werewolf(sex, race, level, danger, attack, health, armor, job)

        name = input("Choose your name or get it by random (Type 'random'): ")
        name = re.sub(r'\s', '', name.lower())
        if name != 'random':
            character.set_name(name)
        # character.print_stats()
        return character

    def start_game(self):
        print("game started")
        print("\n")
        self.command()
        # TODO: starting game and a plot
        sys.exit()

    def continue_game(self):
        print("game continues")
        # TODO: come up with continueing (using progress bar maybe...)
        sys.exit()

    def save_game(self):
        print("game saved")
        # TODO: come up with saving
        sys.exit()

    def progress_bar(self):
        ratio = self.progress // self.max_progress
        bar = ''
        for i in range(0, ratio):
            bar += '+'
        for i in range(ratio, 10):
            bar += '-'
        return bar

    def menu(self, first = False, state = 'main'):
        choices = ('1', '2', '3')
        checks = ('y', 'n')
        if not first:
            self.clear_screen()
        if state == 'pause':
            print('{:*^30}'.format(' Pause '))
            print('{}'.format('1. Continue'))
            print('{}'.format('2. Load game'))
            print('{}'.format('3. Save game'))
            print('{}'.format('4. Quit'))
        else:
            print('{:*^30}'.format(' Main menu '))
            print('{}'.format('1. Game start'))
            print('{}'.format('2. Load game'))
            print('{}'.format('3. Quit'))

        print('\n\nYour progress bar: {}'.format(self.progress_bar()))
        choice = input("\n")
        while not choice.lower() in choices:
            choice = input("Choose the number of your answer please.\n")
        if choice == '1' and state == 'main':
            self.character = self.create_character()
            self.start_game()
        elif choice == '1' and state == 'pause':
            self.continue_game()
        elif choice == '2':
            self.load_game()
        elif choice == '3' and state == 'pause':
            self.save_game()
        else:
            check = input("Are you sure you want to quit? (y/n)\n")
            while not check.lower() in checks:
                check = input("Choose the your answer correctly please.\n")

            if check == 'y':
                sys.exit()
            elif state == 'pause':
                self.menu(state = 'pause')
            else:
                self.menu()
