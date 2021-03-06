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

from logger import logger

class main:
    session_name = 'session.txt'
    session = logger(session_name)

    progress = 0
    max_progress = 10

    data = []
    file_saves = 'save_info.txt'

    weapons = ('sword', 'knife')
    armors  = ('chainmail', 'platemail')
    boots   = ('leather boots', 'steel boots')

    items = ( weapons, armors, boots )

    def __init__(self, creating = False):
        # TODO: init function
        if creating:
            print("hi")
            self.menu()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.session.clear()

    def loading(t = 1):

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

        try:
            name = input("Choose your name or get it by random (Type 'random' or nothing): ")
            name = re.sub(r'\s', '', name.lower())
            if name != 'random':
                character.set_name(name)
        finally:
            return character

    def game(self, game_data = data):
        while True:
            self.clear_screen()
            self.Field.show()
            self.define()

    def start_game(self):
        self.character = self.create_character()
        self.show('stats')
        self.Field = field(self.character)
        self.status = 'moving'
        self.game()

    def load_screen(self):
        temp = self.session
        self.ession.close()

        load = open(self.session_name, 'r')
        for line in load:
            if line != '\n':
                print(line, end='')
        load.close()

        self.session = temp
        temp.close()

    def continue_game(self):
        print("game continues")
        # TODO: come up with continueing (using progress bar maybe...)
        self.session.close()
        sys.exit()

    def load_game(self, menu_state):
        self.clear_screen()
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

    def save_game(self, menu_state = 'pause'):
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
        self.session.close()
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
                    self.session.close()
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
                    self.session.close()
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
            choice = input("Choose the number of an option or type 'info'/'help' please.\n")
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
            self.load_sceen()
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
                self.session.close()
                sys.exit()
            else:
                self.menu(state)

    def __str__(self):
        data = [  ]
        return data

    def move(self, dir, steps):
        self.Field.character_move(dir, steps)

    def retire(self):
        return True

    def payoff(self, cost):
        return True

    def use(self, item):
        return True

    def equip(self, item):
        return True

    def unequip(self, item):
        return True

    def show(self, keyword):
        if not keyword in self.show_keywords:
            return False
        if keyword == 'stats':
            self.clear_screen()
            print(self.character)
            go = input("Type anything when you are ready...\n")
            self.clear_screen()
        return True

    def attack(self, dir):
        return True

    def defend(self):
        return True

    def defend(self):
        return True

# Here comes shell module commands!
    prompt = 'cmd>> '
    error = '*** '
    help = "\nType 'info'/'help' to see what you can do."

    directions = ( 'left', 'right', 'up', 'down' )

    checks = ( 'y', 'n', 'yes', 'no' )


    info_cmd_list = { 'continue' : "Continues a game after pause or loading the last saving.\n\nSyntax: <continue>\n",
                      'start' : "Starts a new game.\n\nSyntax: <start>\n",
                      'save' : "Saves current game session.\n\nSyntax: <save>\n",
                      'load' : "Loads a game from your saves.\n\nSyntax: <load>\n",
                      'show' : "Shows the statistics of anything you want to know.\n\nSyntax: <show> <stats>/<log>/<saves>\n\nstats: statistics of your character\nlog: statistics of the ingame data\nsaves: names of files you can load.\n",
                      'attack' : "Calling your character to attack the nearest enemy.\n\nSyntax: <attack> <dir=>\n\ndir: direction ({}).\n".format(directions),
                      'defend' : "Calling your character to defend from the enemy.\n\nSyntax: <defend>\n",
                      'retire' : "Calling your character to retire from the battle. The enemy won't be defeated.\n\nSyntax: <retire>\n",
                      'payoff' : "Calling your character to pay off from your enemy. The enemy will be considered as defeated.\n\nSyntax: <payoff> <cost=>\n\ncost: amount of money you are going to pay.\n",
                      'go' : "Calling your character to move to the specified place.\n\nSyntax: <go> <dir=> <steps=>\n\ndir: direction {}.\nsteps: the quantity of steps you want your character to do (must be an integer number)\n".format(directions),
                      'move' : "The same as <go>.\n\nSyntax: <move> <dir=> <steps=>\n\ndir: direction {}.\nsteps: the quantity of steps you want your character to do (must be an integer number)\n".format(directions),
                      'buy' : "Allows you to buy an item from the list of available.\n\nSyntax: <buy> <item=>\n",
                      'sell' : "Allows you to sell an item from your inventory.\n\nSyntax: <sell> <item=>\n",
                      'use' : "Allows you to use an item from your inventory.\n\nSyntax: <use> <item=>\n",
                      'equip' : "Equips an item from your inventory (only if the slot is empty).\n\nSyntax: <equip> <item=>\n",
                      'unequip' : "Unequips an item and puts it to your inventory.\n\nSyntax: <unequip> <item=>\n" }

    cmd_list = ( 'continue', 'start', 'save', 'load', 'attack', 'defend', 'retire',
                 'payoff', 'go', 'move', 'buy', 'sell', 'pause', 'quit', 'equip',
                 'unequip', 'show', 'use', 'help', 'info' )

    moving_list = ( 'pause', 'use', 'save', 'attack', 'go', 'move', 'equip', 'unequip')
    fight_list = ( 'pause', 'use', 'retire', 'payoff' )
    menu_list = ( 'continue', 'start', 'load' )
    pause_list = ( 'continue', 'load', 'save' )
    shop_list = ( 'pause', 'buy', 'sell' )
    anywhere = ( 'help', 'info', 'quit', 'show' )

    show_keywords = ( 'stats', 'log', 'saves' )

    def __init__(self, status = 'main'):
        self.change_status(status)

    def change_status(self, status = 'main'):
        self.status = status

    def define(self):
        correct = False
        while not correct:
            cmd = input(self.prompt)
            cmd = self.parse(cmd)
            if not cmd:
                continue

            main_cmd = cmd[0]

            if main_cmd in self.fight_list and self.status == 'fight':
                correct = self.do_fight(cmd)
            elif main_cmd in self.menu_list and self.status == 'main':
                correct = self.do_main(cmd)
            elif main_cmd in self.pause_list and self.status == 'pause':
                correct = self.do_pause(cmd)
            elif main_cmd in self.moving_list and self.status == 'moving':
                correct = self.do_moving(cmd)
            elif main_cmd in self.shop_list and self.status == 'shop':
                correct = self.do_shop(cmd)
            elif main_cmd in self.anywhere:
                correct = self.do(cmd, self.status)
            else:
                print("{} This command is unavailable right now. {}".format(self.error, self.help))
                continue
            if correct:
                return correct

    def parse(self, cmd):
        cmd = cmd.lower()
        cmd = cmd.split()
        try:
            cmd_check = cmd[0]
            if not cmd_check in self.cmd_list:
                print("{} Incorrect command. {}".format(self.error, self.help))
                return False
            elif (cmd_check == 'help' or cmd_check == 'info') and len(cmd) == 1:
                self.info()
                return False
            else:
                return cmd
        except:
            print("{} Incorrect type of the command (#2). {}".format(self.error, self.help))
            return False

    def info(self):
        print("\nCommand list:\n", end='{:+^120}'.format('+'))
        for key in self.info_cmd_list.keys():
            if self.status == 'menu' and key in self.menu_list or self.status == 'pause' and key in self.pause_list or self.status == 'fight' and key in self.fight_list or self.status == 'moving' and key in self.moving_list or self.status == 'shop' and key in self.shop_list:
                print(colored(str(key), 'green'), end=': ')
                print(colored(self.info_cmd_list[key]), end='{:-^120}'.format('-'))
            else:
                print(str(key), end=': ')
                print(self.info_cmd_list[key], end='{:-^120}'.format('-'))

    def do_fight(self, cmd):
        q_of_commands = { 'pause' : 1,
                          'use' : 2,
                          'retire' : 1,
                          'payoff' : 2 }
        main_cmd = cmd[0]
        try:
            if main_cmd in q_of_commands.keys() and len(cmd) == q_of_commands[main_cmd]:
                if main_cmd == 'pause':
                    self.menu('pause')
                    return True
                elif main_cmd == 'retire':
                    self.retire()
                    return is_able
                elif main_cmd == 'payoff' and int(cmd[1]):
                    cost = cmd[1]
                    self.payoff(cost)
                    return is_able
                elif main_cmd == 'use':
                    item = cmd[1]
                    self.use(item)
                    return is_able
            else:
                print("{} Wrong quantity of command keywords. {}".format(self.error, self.help))
                return False
        except:
            print("{} Wrong type of command keyword. {}".format(self.error, self.help))
            return False

    def do_main(self, cmd):
        q_of_commands = { 'continue' : 1,
                          'start' : 1,
                          'load' : 1 }
        main_cmd = cmd[0]
        if main_cmd in q_of_commands.keys() and len(cmd) == q_of_commands[main_cmd]:
            if main_cmd == 'continue':
                self.continue_game()
            if main_cmd == 'start':
                self.start_game()
            if main_cmd == 'load':
                self.load_game('main')
        else:
            return False
        return True

    def do_pause(self, cmd):
        q_of_commands = { 'continue' : 1,
                          'load' : 1,
                          'save' : 1 }
        main_cmd = cmd[0]
        if main_cmd in q_of_commands.keys() and len(cmd) == q_of_commands[main_cmd]:
            if main_cmd == 'continue':
                self.continue_game()
            if main_cmd == 'save':
                self.save_game('pause')
            if main_cmd == 'load':
                self.load_game('pause')
        else:
            return False
        return True

    def do_moving(self, cmd):
        q_of_commands = { 'pause' : 1,
                          'use' : 2,
                          'save' : 1,
                          'attack' : 2,
                          'go' : 3,
                          'move' : 3,
                          'equip' : 2,
                          'unequip' : 2 }
        main_cmd = cmd[0]
        try:
            if main_cmd in q_of_commands.keys() and len(cmd) == q_of_commands[main_cmd]:
                if main_cmd == 'pause':
                    self.menu('pause')
                    return True
                elif main_cmd == 'save':
                    self.save_game()
                    return True
                elif main_cmd == 'attack' and cmd[1] in self.directions:
                    dir = cmd[1]
                    self.attack(self.status, dir)
                    return is_able
                elif main_cmd == 'use':
                    item = cmd[1]
                    self.use(item)
                    return is_able
                elif main_cmd == 'equip':
                    item = cmd[1]
                    self.equip(item)
                    return is_able
                elif main_cmd == 'unequip':
                    item = cmd[1]
                    self.equip(item)
                    return is_able
                elif (main_cmd == 'move' or main_cmd == 'go') and int(cmd[2]):
                    dir = cmd[1]
                    steps = cmd[2]
                    return self.move(dir, steps)
            else:
                print("{} Wrong quantity of command keywords. {}".format(self.error, self.help))
                return False
        except:
            print("{} Wrong type of command keyword. {}".format(self.error, self.help))
            return False
        return True

    def do_shop(self, cmd):
        q_of_commands = { 'pause' : 1,
                          'buy' : 2,
                          'sell' : 2 }
        main_cmd = cmd[0]
        try:
            if main_cmd in q_of_commands.keys() and len(cmd) == q_of_commands[main_cmd]:
                if main_cmd == 'pause':
                    self.menu('pause')
                    return True
                elif main_cmd == 'buy':
                    item = cmd[1]
                    self.buy(item)
                    return is_able
                elif main_cmd == 'sell':
                    item = cmd[1]
                    self.sell(item)
                    return is_able
            else:
                print("{} Wrong quantity of command keywords. {}".format(self.error, self.help))
                return False
        except:
            print("{} Wrong type of command keyword. {}".format(self.error, self.help))
            return False
        return True

    def do(self, cmd, status):
        q_of_commands = { 'quit' : 1,
                          'help' : 1,
                          'info' : 1,
                          'show' : 2 }
        main_cmd = cmd[0]
        if main_cmd in q_of_commands.keys() and len(cmd) == q_of_commands[main_cmd]:
            if main_cmd == 'quit':
                check = input("Are you sure you want to quit? (y/n)\n")
                while not check.lower() in self.checks:
                    check = input("Choose the your answer correctly please.\n")
                if check == 'y' or check == 'yes':
                    sys.exit()
                    return False
                else:
                    return False
            elif main_cmd == 'help' or main_cmd == 'info':
                item = cmd[1]
                self.info(status)
                return False
            elif main_cmd == 'show':
                keyword = cmd[1]
                self.show(keyword)
                return is_able
        else:
            print("{} Wrong quantity of command keywords. {}".format(self.error, self.help))
            return False
        return True
