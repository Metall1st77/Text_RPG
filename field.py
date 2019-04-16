import random
import sys
import math
import time

class field():
    biomes = ('desert', 'desert')

    symbs_for_biomes = { 'desert' : '.' }

    full_field = []
    f_rows = 50
    f_cols = 70

    visible_field = []
    v_rows = 20
    v_cols = 30

    def __init__(self, level = 1, enemies = 0, biome = random.choice(biomes)):
        for row in range(self.f_rows):
            self.full_field.append([])
            for col in range(self.f_cols):
                self.full_field[row].append(self.symbs_for_biomes[biome])

        for row in range(self.v_rows):
            self.visible_field.append([])
            for col in range(self.v_cols):
                self.visible_field[row].append(self.full_field[row][col])

    def show(self, full = False):
        if full:
            for i in range(self.f_rows):
                for k in range(self.f_cols):
                    print(self.full_field[i][k], end='')
                print()
        else:
            for i in range(self.v_rows):
                for k in range(self.v_cols):
                    print(self.visible_field[i][k], end='')
                print()
