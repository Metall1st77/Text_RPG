import random
import sys
import math
import time
import re
import os

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

    data = [ 'progress : ' + str(progress) ]
    file_saves = 'save_info.txt'

    level_enemy_count = [3, 4, 6, 8, 11, 15]

    directions = ( ('left',  'a'),
                   ('right', 'd'),
                   ('up',    'w'),
                   ('down',  's') )

    weapons = ('sword', 'knife')
    armors  = ('chainmail', 'platemail')
    boots   = ('leather boots', 'steel boots')

    items = ( weapons, armors, boots )

    commands = { 'menu'     : ('continue', 'new', 'load'),
                 'pause'    : ('continue', 'restart', 'save', 'load'),
                 'fight'    : ('attack', 'defend', 'retire', 'payoff'),
                 'walk'     : ('go', 'move'),
                 'shop'     : ('buy', 'sell'),
                 'anywhere' : ('pause', 'quit'),
                 'free'     : ('equip', 'unequip') }

    def __init__(self):
        # TODO: init function
        self.menu('pause')
        return

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # def loading(t = 1):
    #     # clear_screen()
    #     k = 0
    #     print("Loading", end='')
    #     while k < 3:
    #         time.sleep(1)
    #         print(".", end='')
    #         k += 1


    def command(self, status = 'menu'):
        # status may have values: 'menu', 'pause', 'fight', 'walk', 'shop' and 'free'
        cmd = input()
        cmd = re.sub(r'\s', ' ', cmd.lower())
        cmd = cmd.split()
        while not cmd[0] in self.commands[status]:
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

    def show_stats(self, character):
        self.clear_screen()
        print(character)

    def game(self):
        # TODO: GAME!
        return

    def start_game(self):
        self.character = self.create_character()
        self.show_stats(self.character)
        Field = field(self.character, enemies = self.level_enemy_count[0])
        # Main loop
        self.game()
        print("game started")
        print("\n")
        # TODO: starting game and a plot
        return

    def load_game(self, load):
        print("game loading")
        # TODO: game Loading
        return

    def continue_game(self):
        print("game continues")
        # TODO: come up with continueing (using progress bar maybe...)
        sys.exit()

    def save_game(self):
        self.clear_screen()
        checks = ('y', 'n', 'yes', 'no')

        save = input("Type the name of the file for saving: ")
        file = open(self.file_saves, 'r')
        saves = []
        for load_no in file:
            saves.append(load_no[:len(load_no) - 1])
        file.close()

        while save in saves:
            check = input("This name is already in use. Are you sure you want to overwrite the save? (Type y/n)\n")
            while not check in checks:
                check = input("Type 'y' or 'n' please.\n")
            if check[0] == 'n':
                self.save_game()
            else:
                break

        file = open(self.file_saves, 'r')
        d = [line.strip() for line in file]
        file.close()

        file = open(self.file_saves, 'w')
        for i in range(len(d)):
            file.write(d[i] + '\n')
        file.write(save)
        file.close()

        save_name = 'saves/' + save + '.txt'
        s = open(save_name, 'w')
        # s.write(self.data)
        # s.write(self.character)
        s.close()

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

    def menu(self, state = 'main'):
        self.clear_screen()
        current_state = state
        choices = ('1', '2', '3', '4', 'continue', 'save', 'load', 'start', 'quit', 'info')
        checks = ('y', 'n', 'yes', 'no')

        main_choices = ('start', 'load', 'quit')
        pause_choices = ('continue', 'load', 'save', 'quit')

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
        choice = input("Choose the number of your choice or type 'info' please.\n")
        while not choice.lower() in choices:
            choice = input("Choose the number of your choice or type 'info' please.\n")
            choice = choice.lower()
        if (choice == '1' or choice == 'start') and state == 'main':
            self.clear_screen()
            self.start_game()

        elif (choice == '1' or choice == 'continue') and state == 'pause':
            self.clear_screen()
            self.continue_game()

        elif choice == '2' or choice == 'load':
            self.clear_screen()
            print("\nThe following saves are available to you:\n")
            file = open(self.file_saves, 'r')

            no = 1
            saves = ['back']
            for load_no in file:
                print('{}. {}'.format(no, load_no), end='')
                saves.append(load_no[:len(load_no) - 1])
                no +=1
            load_file = input("\nChoose the name of the file or type 'back': ")
            while not load_file in saves:
                load_file = input("Choose the name of the file correctly!\n")
            if load_file == 'back':
                self.menu(current_state)
            else:
                self.load_game(load_file)

        elif (choice == '3' or choice == 'save') and state == 'pause':
            self.save_game()

        elif choice == 'info':
            if state == 'main':
                print("The following commands are available for you now: {}.".format(main_choices))
            else:
                print("The following commands are available for you now: {}.".format(pause_choices))
            back = input("Type anything when you are ready...\n")
            self.menu(current_state)

        else:
            check = input("Are you sure you want to quit? (y/n)\n")
            while not check.lower() in checks:
                check = input("Choose the your answer correctly please.\n")

            if check == 'y' or check == 'yes':
                sys.exit()
            else:
                self.menu(current_state)
