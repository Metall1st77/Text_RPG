import random
import sys
import math
import time
import re
import os

from creatures.creature import creature
from creatures.human    import human
from creatures.werewolf import werewolf
from creatures.treant   import treant
from creatures.tech     import tech
from creatures.demon    import demon

from field import field
from fight import fight

class main:
    progress = 0
    max_progress = 10

    data = []
    file_saves = 'save_info.txt'

    # commands = { 'menu'     : ('continue', 'new', 'load'),
    #              'pause'    : ('continue', 'restart', 'save', 'load'),
    #              'fight'    : ('attack', 'defend', 'retire', 'payoff'),
    #              'walk'     : ('go', 'move'),
    #              'shop'     : ('buy', 'sell'),
    #              'anywhere' : ('pause', 'quit'),
    #              'free'     : ('equip', 'unequip') }

    weapons = ('sword', 'knife')
    armors  = ('chainmail', 'platemail')
    boots   = ('leather boots', 'steel boots')

    items = ( weapons, armors, boots )

    def __init__(self):
        # TODO: init function
        self.Shell = shell()
        self.Shell.define()
        # self.character = self.create_character()
        # self.menu('pause')
        self.menu()
        return

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def loading(t = 1):
        # clear_screen()
        k = 0
        print("Loading", end='')
        while k < 3:
            time.sleep(1)
            print(".", end='')
            k += 1

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

        name = input("Choose your name or get it by random (Type 'random' or nothing): ")
        name = re.sub(r'\s', '', name.lower())
        name += ' '
        if name != 'random' or name != ' \n':
            character.set_name(name)
        # character.print_stats()
        return character

    def show_stats(self, character):
        self.clear_screen()
        print(character)
        go = input("Type anything when you are ready...\n")
        self.clear_screen()

    def game(self, game_data = data):
        # TODO: GAME!
        self.clear_screen()

    def start_game(self):
        self.character = self.create_character()
        self.show_stats(self.character)
        Field = field(self.character)
        # Main loop
        self.game()

        print("game started")
        print("\n")
        # TODO: starting game and a plot
        return

    def reload_screen(self):
        print("screen reloaded")
        return

    def continue_game(self):
        print("game continues")
        # TODO: come up with continueing (using progress bar maybe...)
        sys.exit()

    def load_game(self, menu_state):
        file = open(self.file_saves, 'r')
        no = 0
        for line in file:
            no += 1
        saves = ['back', 'delete']
        file.close()

        if no == 0:
            print("There are no any saves!")
            input("Type anything when you are ready...\n")
            self.menu(menu_state)

        print("The following saves are available to you:\n")

        no = 1
        file = open(self.file_saves, 'r')
        for load_no in file:
            print('{}. {}'.format(no, load_no), end='')
            saves.append(load_no[:len(load_no) - 1])
            no += 1
        file.close()

        load_file = input("\nChoose the name of the file, type 'back' to go back to menu or type 'delete' to remove your saving: ")
        while not load_file in saves:
            load_file = input("Choose the name of the file correctly!\n")

        if load_file.lower() == 'back':
            self.menu(menu_state)
        elif load_file.lower() == 'delete':
                self.delete_saving(menu_state)
                self.menu(menu_state)
        else:
            load_file = 'saves/' + load_file + '.txt'
            load_file = open(load_file, 'r')
            self.data = [line.strip() for line in load_file]
            # self.game(self.data)
            self.game()

        return

    def save_game(self, menu_state):
        checks = ('y', 'n', 'yes', 'no')
        try:
            save = input("Type the name of the file for saving or type 'back' to go to the menu: ")
            save = re.sub(r'\s', '', save.lower())
            if save == 'back':
                self.menu(menu_state)

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
                if save != d[i]:
                    file.write(d[i] + '\n')
            file.write(save + '\n')
            file.close()

            save_name = 'saves/' + save + '.txt'
            s = open(save_name, 'w')
            # s.write(self.data)
            s.write(str(self.character))
            s.close()
        except:
            print("*** Some error was accured!")

        # TODO: come up with saving
        sys.exit()

    def delete_saving(self, menu_state, delete = None):
        dir = 'saves/'
        ending = '.txt'
        if delete == None:
            file = open(self.file_saves, 'r')
            saves = [ 'back', 'all' ]
            for load_no in file:
                saves.append(load_no[:len(load_no) - 1])
            file.close()

            delete = input("Type the name of the file for removing (type 'all' to delete everything) or 'back' to go back to menu: ")
            while not delete in saves:
                delete = input("Type the name of the file for removing (type 'all' to delete everything) or 'back' to go back to menu correctly!\n")
            if delete.lower() == 'back':
                self.menu(menu_state)
            elif delete.lower() == 'all':
                file = open(self.file_saves, 'w')
                file.close()

                try:
                    saves = saves[2:]
                    for file in saves:
                        os.remove(dir + file + ending)
                except:
                    print("Something went wrong!")
                    sys.exit()
                print("All saves have been removed!")

            else:
                file = open(self.file_saves, 'r')
                d = [line.strip() for line in file]
                file.close()

                file = open(self.file_saves, 'w')
                for i in range(len(d)):
                    if d[i] == delete:
                        continue
                    file.write(d[i] + '\n')
                file.close()

                try:
                    os.remove(dir + delete + ending)
                except:
                    print("Something went wrong!")
                    sys.exit()
                print("Save has been removed!")

    def progress_bar(self):
        ratio = self.progress // self.max_progress
        bar = ''
        for i in range(0, ratio):
            bar += '+'
        for i in range(ratio, 10):
            bar += '-'
        return bar

    def menu(self, state = 'main'):
        Shell.status = state
        self.clear_screen()
        choices = ('1', '2', '3', '4', 'continue', 'save', 'load', 'start', 'quit')
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
        choice = input("\nChoose the number of an option please.\n")
        while not choice.lower() in choices:
            choice = input("Choose the number an option or type 'info'/'help' please.\n")
            choice = choice.lower()
            if choice == 'info' or choice == 'help':
                if state == 'main':
                    print("The following commands are available for you now: {}.".format(main_choices))
                else:
                    print("The following commands are available for you now: {}.".format(pause_choices))

        if (choice == '1' or choice == 'start') and state == 'main':
            self.clear_screen()
            self.start_game()

        elif (choice == '1' or choice == 'continue') and state == 'pause':
            self.clear_screen()
            self.continue_game()

        elif choice == '2' or choice == 'load':
            self.clear_screen()
            self.load_game(state)

        elif (choice == '3' or choice == 'save') and state == 'pause':
            self.clear_screen()
            self.save_game(state)

        else:
            check = input("Are you sure you want to quit? (y/n)\n")
            while not check.lower() in checks:
                check = input("Choose the your answer correctly please.\n")

            if check == 'y' or check == 'yes':
                sys.exit()
            else:
                self.menu(state)

    def __str__(self):
        data = [  ]
        return data

    def move(self, dir, steps):
        print("You walked {} steps {}".format(steps, dir))



# Here comes Cmd module commands!

class shell:
    prompt = 'cmd>> '
    error = '*** '

    status = None
    in_game = False
    in_shop = False

    directions = ( 'left', 'right', 'up', 'down' )

    info_cmd_list = { 'continue' : "Continues a game after pause or loading the last saving.\nSyntax: <continue>\n",
                      'new' : "Starts a new game.\nSyntax: <new>\n",
                      'save' : "Saves current game session.\nSyntax: <save> <name=>\n",
                      'load' : "Loads a game from your saves.\nSyntax: <load> <name=>\n",
                      'show' : "Shows the statistics of anything you want to know.\nSyntax: <show> <stats/log/saves>\nstats: statistics of your character\nlog: statistics of the ingame data\nsaves: names of files you can load.\n",
                      'attack' : "Calling your character to attack the nearest enemy.\nSyntax: <attack> <dir=>\ndir: direction ({}).\n".format(directions),
                      'defend' : "Calling your character to defend from the enemy.\nSyntax: <defend>\n",
                      'retire' : "Calling your character to retire from the battle. The enemy won't be defeated.\nSyntax: <retire>\n",
                      'payoff' : "Calling your character to pay off from your enemy. The enemy will be considered as defeated.\nSyntax: <payoff> <cost=>\ncost: amount of money you are going to pay.\n",
                      'go' : "Calling your character to move to the specified place.\nSyntax: <go> <dir=> <steps=>\ndir: direction ({}).\nsteps: the quantity of steps you want your character to do (must be an integer number)\n".format(directions),
                      'move' : "The same as <go>.\nSyntax: <move> <dir=> <steps=>\ndir: direction ({}).\nsteps: the quantity of steps you want your character to do (must be an integer number)\n".format(directions),
                      'buy' : "Allows you to buy an item from the list of available.\nSyntax: <buy> <item=>\n",
                      'sell' : "Allows you to sell an item from your inventory.\nSyntax: <sell> <item=>\n",
                      'use' : "Allow you to use an item from your inventory.\nSyntax: <use> <item=>\n",
                      'equip' : "Equips an item from your inventory (only if the slot is empty).\nSyntax: <equip> <item=>\n",
                      'unequip' : "Unequips an item and puts it to your inventory.\nSyntax: <unequip> <item=>" }

# TODO: Make info look normal...

    cmd_list = ( 'continue', 'new', 'save', 'load', 'attack', 'defend', 'retire',
                 'payoff', 'go', 'move', 'buy', 'sell', 'pause', 'quit', 'equip',
                 'unequip', 'show', 'use', 'help', 'info' )

    in_game_list = ( 'attack', 'defend', 'retire', 'payoff', 'go', 'move', 'buy',
                     'sell', 'equip', 'unequip')

    def define(self):
        correct = False
        while not correct:
            cmd = input(self.prompt)
            cmd = cmd.lower()
            cmd = cmd.split()
            try:
                main_cmd = cmd[0]
                if not main_cmd in self.cmd_list:
                    print("{} Incorrect command. Type 'help' or 'info' to see the command list.".format(self.error))
                else:
                    if (main_cmd == 'help' or main_cmd == 'info') and len(cmd) == 1:
                        print("Command list:\n{}\n".format(str(self.info_cmd_list)))
                    elif main_cmd in self.in_game_list and not in_game:
                        print("{} This command is unavailable right now.".format(self.error))
            except:
                print("{} Incorrect command. Type 'help' or 'info' to see the command list.".format(self.error))

    def go(self, cmd):
        arg = arg.lower()
        moving = arg.split()
        directions = ('left', 'right', 'up', 'down')
        if len(moving) != 2:
            print("{} Wrong command. Expected direction and quantity of steps.".format(self.error))
            self.define()

        dir = moving[0]
        steps = moving[1]
        if not moving[0] in directions:
            print("{} Wrong direction. Expected 'left', 'right', 'up' or 'down'.".format(self.error))
            self.define()

        try:
            steps = int(steps)
            dir = str(dir)
            main().move(dir, steps)
        except:
            print("{} Wrong quantity of steps. Expected an integer number of steps.".format(self.error))
            self.define()
