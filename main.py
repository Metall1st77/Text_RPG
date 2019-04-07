import random
import sys
import math
import time


def clear_screen():
    for i in range(0, 50):
        print("\n")

def loading(t = 1):
    # clear_screen()
    print("Loading...", end='')
    time.sleep(1)


def start_game():
    print("game started")
    sys.exit()

def continue_game():
    print("game continues")
    sys.exit()

def menu(first = False, state = 'main'):
    choises = ('1', '2', '3')
    checks = ('y', 'n')
    if not first:
        clear_screen()
    if state == 'pause':
        print('{:*^30}'.format(' Pause '))
    else:
        print('{:*^30}'.format(' Main menu '))
    print('{}'.format('1. Game start'))
    print('{}'.format('2. Continue'))
    print('{}'.format('3. Quit'))
    choise = input("\n")
    while not choise in choises:
        choise = input("Choose the number of your answer please.\n")
    if choise == '1':
        start_game()
    elif choise == '2':
        continue_game()
    else:
        check = input("Are you sure you want to quit? (y/n)\n")
        while check not in checks:
            check = input("Choose the number of your answer please.\n")

        if check == 'y':
            sys.exit()
        else:
            menu()
