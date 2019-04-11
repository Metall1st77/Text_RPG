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

from field import field
from fight import fight

class main:
    progress = 0
    max_progress = 10

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

    def command(self, keyword, possibility_to_move = True, possibility_to_fight = False,
        possibility_to_defend = False):
        keyword = keyword.lower()
        if (keyword == 'go' or keyword == 'move') and possibility_to_move:
            move(direction())
        elif (keyword == 'attack' or keyword == 'fight') and possibility_to_fight:
            attack()
        elif keyword == 'defend' and possibility_to_defend:
            defend()
        elif keyword == 'pause':
            menu(state = 'pause')
        # TODO:

    def attack(self):
        # TODO: attack function
        return

    def defend(self):
        # TODO: defend function
        return

    def direction(self):
        directions = ('up', 'down', 'left', 'right', 'w', 'a', 's', 'd')
        direction = input("Where do you want to go?\n(Type up/left/down/right, or use w/a/s/d)\n")
        while not direction.lower() in directions:
            direction = input("Choose the your answer correctly please.\n")
        return direction

    def move(self, direction):
        if direction == 'left' or direction == 'a':
            # TODO: left
            return
        elif direction == 'up' or direction == 'w':
            # TODO: up
            return
        elif direction == 'down' or direction == 's':
            # TODO: down
            return
        elif direction == 'right' or direction == 'd':
            # TODO: right
            return
        else:
            print("There are some problems...")
            sys.exit()

    def start_game(self):
        print("game started")
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
            self.start_game()
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
