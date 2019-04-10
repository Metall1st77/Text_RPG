import random
import sys
import math
import time

class field():
    biomes = ('desert', 'desert')

    symbs_for_biomes = { 'desert' : '.' }

    full_field = []
    visible_field = []

    def __init__(self, enemies = 0, biome = random.choice(biomes)):
        for i in range(50):
            self.full_field.append([])
            for k in range(70):
                self.full_field[i].append(self.symbs_for_biomes[biome])

    def show():
        for i in range(50):
            for k in range(70):
                print(self.full_field[i][k], end='')
            print()
