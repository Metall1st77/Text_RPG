import random
import sys
import math
import time

progress = 0
max_progress = 10

def clear_screen():
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

def command(keyword, possibility_to_move = True, possibility_to_fight = False,
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

def attack():
    # TODO: attack function
    return

def defend():
    # TODO: defend function
    return

def direction():
    directions = ('up', 'down', 'left', 'right', 'w', 'a', 's', 'd')
    direction = input("Where do you want to go?\n(Type up/left/down/right, or use w/a/s/d)\n")
    while not direction.lower() in directions:
        direction = input("Choose the your answer correctly please.\n")
    return direction

def move(direction):
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

def start_game():
    print("game started")
    # TODO: starting game and a plot
    sys.exit()

def continue_game():
    print("game continues")
    # TODO: come up with continueing (using progress bar maybe...)
    sys.exit()

def progress_bar():
    ratio = progress // max_progress
    bar = ''
    for i in range(0, ratio):
        bar += '+'
    for i in range(ratio, 10):
        bar += '-'
    return bar


def menu(first = False, state = 'main'):
    choises = ('1', '2', '3')
    checks = ('y', 'n')
    if not first:
        clear_screen()
    if state == 'pause':
        print('{:*^30}'.format(' Pause '))
        print('{}'.format('1. Continue'))
        print('{}'.format('2. Quit'))
    else:
        print('{:*^30}'.format(' Main menu '))
        print('{}'.format('1. Game start'))
        print('{}'.format('2. Continue'))
        print('{}'.format('3. Quit'))

    print('\n\nYour progress bar: {}'.format(progress_bar()))
    choise = input("\n")
    while not choise.lower() in choises:
        choise = input("Choose the number of your answer please.\n")
    if choise == '1' and state == 'main':
        start_game()
    elif choise == '2' and state == 'main' or choise == '1' and state == 'pause':
        continue_game()
    else:
        check = input("Are you sure you want to quit? (y/n)\n")
        while not check.lower() in checks:
            check = input("Choose the your answer correctly please.\n")

        if check == 'y':
            sys.exit()
        elif state == 'pause':
            menu(state = 'pause')
        else:
            menu()
