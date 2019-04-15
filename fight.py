class fight():
    def __init__(self, file, character, enemy, init_by_character = True):
        f = open(file, 'r')
        for line in f:
            print(line, end='')
        if init_by_character:
            print("{} has just attacked an enemy {}!".format(character.name, enemy.race))
        else:
            print("An enemy {} has just attacked {}!".format(enemy.race, character.name))

# Fight = fight('demon1.txt')
