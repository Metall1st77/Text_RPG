import random
import sys
import math
import time

class field():
    char_model = 'X'

    biomes = ('desert', 'snow', 'swamp', 'ground')

    symbs_for_biomes = { 'desert' : '.',
                         'snow'   : '\'',
                         'swamp'  : ',',
                         'ground' : '+' }

    level_enemy_count = [3, 4, 6, 8, 11, 15, 17, 19, 20, 21]

    full_field = []
    f_rows = 50
    f_cols = 70

    visible_field = []
    v_rows = 20
    v_cols = 30

    random_percentage = 0.25
    area = f_cols * f_rows

    char_pos_X = 0
    char_pos_Y = 0
    symbol_under_character = ''

    def __init__(self, character, level = 0, enemies = level_enemy_count[0], load = False):
        biomes = self.__biomes_area_count()
        if load:
            self.load_field()
        else:
            self.create_field(character, level, enemies, biomes)

    def load_field(self):
        return

    def create_field(self, character, level, enemies, biomes):
        for row in range(self.f_rows):
            for col in range(self.f_cols):
                if row == self.char_pos_X and col == self.char_pos_Y:
                    continue

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

    def __biomes_area_count(self):
        biomes_count = random.randint(2, len(self.biomes))
        biomes_on_field = []
        biomes_area = []

        biome_area = self.area // biomes_count
        rate = int(self.random_percentage * biome_area // 1)

        min_biome_area = biome_area - rate
        max_biome_area = biome_area + rate

        sum_biome_area = 0

        for i in range(0, biomes_count):
            next_biome = random.choice(self.biomes)
            while self.symbs_for_biomes in biomes_on_field:
                next_biome = random.choice(self.biomes)

            if i != biomes_count - 1:
                biomes_on_field.append(next_biome)
                biomes_area.append(random.randint(min_biome_area, max_biome_area))
                sum_biome_area += biomes_area[i]
            else:
                biomes_on_field.append(next_biome)
                biomes_area.append(self.area - sum_biome_area)

        area = dict(zip(biomes_on_field, biomes_area))

        return area

    def __add_character_on_field(self, r, c):
        self.__set_character_pos(r, c)
        return self.char_model

    def __set_character_pos(self, r, c):
        self.char_pos_X = r
        self.char_pos_Y = c

    def character_move():
        return
