import random
import sys
import math
import time

from creatures.creature import creature

class field():
    char_model = 'X'
    no_model = '0'

    biomes = ('desert', 'snow', 'swamp', 'ground', 'forest')

    symbs_for_biomes = { 'desert' : '.',
                         'snow'   : '\'',
                         'swamp'  : ',',
                         'ground' : '+',
                         'forest' : '^' }

    biomes_by_symbs = { '.'   : 'desert',
                        '\'' : 'snow',
                        ','  : 'swamp',
                        '+'  : 'ground',
                        '^'  : 'forest' }

    level_enemy_count = [3, 4, 6, 8, 11, 15, 17, 19, 20, 21]

    full_field = []
    f_rows = 70
    f_cols = 70

    visible_field = []
    v_rows = 30
    v_cols = 30

    random_percentage = 0.25
    area = f_cols * f_rows

    char_pos_X = 0
    char_pos_Y = 0
    symbol_under_character = ''

    def __init__(self, character, level = 0, load = False):
        self.enemies = self.level_enemy_count[level]
        self.current_level = level
        self.character = character
        if load:
            self.load_field()
        else:
            self.__create_field()

    def load_field(self):
        return

    def __create_field(self):
        self._fill_with_nothing(self.no_model)

        biomes = self.__biomes_area_count()
        starting_spots = self.__define_starting_spots(biomes)

        self.__spreading(starting_spots, biomes)

        self._add_character_on_field()


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

    def __update_visible_field(self, down=0, right=0):
        for row in range(self.v_rows):
            self.visible_field.append([])
            for col in range(self.v_cols):
                self.visible_field[row].append(self.full_field[row + right][col + down])

    def __define_starting_spots(self, biomes):
        number_of_points = len(biomes)
        central_point = { 'x' : self.f_rows // 2,
                          'y' : self.f_cols // 2 }
        diagonal = math.sqrt(math.pow(self.f_rows, 2) + math.pow(self.f_cols, 2))
        radius = int(random.randint(20, 30) / 100 * diagonal)
        angle = (2 * math.pi) / number_of_points
        starting_spots = []
        for i in range(number_of_points):
            X = radius * math.cos(angle * i) + central_point['x']
            Y = radius * math.sin(angle * i) + central_point['y']
            spot = (int(X), int(Y))
            starting_spots.append(spot)
        return starting_spots

    def _fill_with_nothing(self, symbol):
        for row in range(self.f_rows):
            self.full_field.append([])
            for col in range(self.f_cols):
                self.full_field[row].append(symbol)

    def __spreading(self, starting_spots, biomes):
        full = False

        i = 0
        for spot in biomes.keys():
            x, y = starting_spots[i][0], starting_spots[i][1]
            self.full_field[x][y] = self.symbs_for_biomes[spot]
            i += 1


        while not full:
            current_spots = []
            for row in range(self.f_rows):
                for col in range(self.f_cols):
                    spot = self.full_field[row][col]
                    nearest = self.__nearest(row, col)
                    if spot == self.no_model and nearest != []:
                        current_spot = (row, col, nearest)
                        current_spots.append(current_spot)

            for spot in range(len(current_spots)):
                x = current_spots[spot][0]
                y = current_spots[spot][1]
                s = random.choice(current_spots[spot][2])
                symbol = s[0]
                self.full_field[x][y] = symbol

            sub_full = True
            for row in range(self.f_rows):
                for col in range(self.f_cols):
                    if self.full_field[row][col] == self.no_model:
                        sub_full = False
                        break
                if not sub_full:
                    break
            if sub_full == True:
                full = True

        # self.show(True)
        return

    def __nearest(self, x, y):
        neighbours = []
        if x != 0 and self.full_field[x - 1][y] != self.no_model:
            spot = (self.full_field[x - 1][y], x - 1, y)
            neighbours.append(spot)
        if y != 0 and self.full_field[x][y - 1] != self.no_model:
            spot = (self.full_field[x][y - 1], x, y - 1)
            neighbours.append(spot)
        if x != self.f_rows - 1 and self.full_field[x + 1][y] != self.no_model:
            spot = (self.full_field[x + 1][y], x + 1, y)
            neighbours.append(spot)
        if y != self.f_cols - 1 and self.full_field[x][y + 1] != self.no_model:
            spot = (self.full_field[x][y + 1], x, y + 1)
            neighbours.append(spot)
        return neighbours

    def __biomes_area_count(self):
        biomes_count = random.randint(2, len(self.biomes))
        biomes_on_field = []
        biomes_area = []

        biome_area = self.area // biomes_count
        rate = int(self.random_percentage * biome_area // 1)

        min_biome_area = biome_area - rate
        max_biome_area = biome_area + rate

        sum_biome_area = 0

        for i in range(biomes_count):
            next_biome = random.choice(self.biomes)
            while next_biome in biomes_on_field:
                next_biome = random.choice(self.biomes)

            if i != biomes_count - 1:
                biomes_on_field.append(next_biome)
                biomes_area.append(random.randint(min_biome_area, max_biome_area))
                sum_biome_area += biomes_area[i]
            else:
                biomes_on_field.append(next_biome)
                biomes_area.append(self.area - sum_biome_area)

        area = dict(zip(biomes_on_field, biomes_area))
        # print(biomes_count)
        # print(biomes_on_field)
        # print(biomes_area)
        # print(area.keys())
        return area

    def _add_character_on_field(self, row=0, col=0):
        self.__set_character_pos(row, col)
        self.full_field[row][col] = self.char_model

        self.__update_visible_field()

    def __set_character_pos(self, row, col):
        pos_X = row
        pos_Y = col
        self.character.set_position(pos_X, pos_Y)
        self.char_pos_X = pos_X
        self.char_pos_Y = pos_Y

    def character_move(self, dir, steps):
        if dir == 'up' and self.char_pos_Y >= steps:
            x = self.char_pos_X
            y = self.char_pos_Y - steps
        elif dir == 'right' and self.char_pos_X + steps <= self.f_cols:
            x = self.char_pos_X + steps
            y = self.char_pos_Y
        elif dir == 'down' and self.char_pos_Y + steps <= self.f_rows:
            x = self.char_pos_X
            y = self.char_pos_Y + steps
        elif dir == 'left' and self.char_pos_X >= steps:
            x = self.char_pos_X - steps
            y = self.char_pos_Y
        else:
            return False
        self.__set_character_pos(x, y)
        self.character.set_position(pos_X, pos_Y)
        return True


if __name__ == '__main__':
    creating_hero = { 'sex' : 'male',
                      'race' : 'human',
                      'level' : '1',
                      'danger' : None,
                      'attack' : '10',
                      'health' : '100',
                      'armor' : '10',
                      'job' : None }
    Hero = creature(**creating_hero)
    Field = field(Hero)
