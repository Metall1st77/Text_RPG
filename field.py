import random
import sys
import math
import time

class field():
    char_model = '+'

    biomes = ('desert', 'snow')

    symbs_for_biomes = { 'desert' : '.',
                         'snow'   : '\'' }

    level_enemy_count = [3, 4, 6, 8, 11, 15, 17, 19, 20, 21]

    char_pos_X = 0
    char_pos_Y = 0

    full_field = []
    f_rows = 50
    f_cols = 70

    visible_field = []
    v_rows = 20
    v_cols = 30

    def __init__(self, character, level = 0, enemies = level_enemy_count[0], biome = random.choice(biomes), load = False):
        if load:
            self.load_field()
        else:
            self.create_field(character, level, enemies, biome)

    def load_field(self):
        return

    def create_field(self, character, level, enemies, biome):
        for row in range(self.f_rows):
            self.full_field.append([])
            for col in range(self.f_cols):
                if row == self.char_pos_X and col == self.char_pos_Y:
                    self.full_field[row].append(self.__add_character_on_field(row, col))
                    continue
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

    def __add_character_on_field(self, r, c):
        self.__set_character_pos(r, c)
        return self.char_model

    def __set_character_pos(self, r, c):
        self.char_pos_X = r
        self.char_pos_Y = c

    def character_move():
        return
