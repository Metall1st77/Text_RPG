import random
import sys
import math

class creature:

    max_level  = 100
    max_attack = 100
    max_health = 100
    max_armor = 100
    max_mana = 100

    job_for_race = {'human' : 'trader',
                    'werewolf' : 'hunter',
                    'treant' : 'forester',
                    'tech' : 'engineer',
                    'demon' : 'devourer'}

    sexes = ('male', 'female')

    male_names = ( 'Avraam', 'Ben', 'Carl', 'Dennis', 'Eagle', 'Franc', 'George',
                   'Henry', 'Iden', 'James', 'Kael', 'Lucas', 'Mark', 'Nicolas',
                   'Odin', 'Pablo', 'Quentin', 'Rafael', 'Sebastian', 'Travis',
                   'Ulric', 'Vincent', 'William', 'Xavier', 'Yann', 'Zac' )
    # TODO: other male names
    female_names = ( 'Alivia', 'Bella', 'Clara', 'Danna', 'Erica', 'Felicia',
                     'Gabrielle', 'Helen', 'Isabella', 'Jasmine', 'Katerina',
                     'Luna', 'Mia', 'Nanacy', 'Olivia', 'Penny', 'Queen', 'Rachel',
                     'Sophia', 'Tacie', 'Unity', 'Victoria', 'Willow', 'Xenia',
                     'Ysera', 'Zenia')
    # TODO: other female names

    jobs = ('none', 'quest', 'helper', 'warrior')
    races = ('human', 'werewolf', 'treant', 'tech', 'demon')
    dangers = ('none', 'unknown', 'safe', 'unstable', 'dangerous')

    item = { 'weapon' : None,
             'armor'  : None,
             'boots'  : None }

    item_strength = { 'weapon' : None,
                      'armor'  : None,
                      'boots'  : None }

    little = 10
    standard = 20
    much = 40
    standard_speed = 50
    damage_by_soul = 3

 # = random.choice(sexes)
 # = random.choice(races)
 # = random.randint(0, max_level)
 # = random.choice(dangers)
 # = random.randint(0, max_attack)
 # = random.randint(1, max_health)
 # = random.randint(0, max_armor)
 # = random.choice(jobs)

    def __init__(self, sex, race, level, danger, attack, health, armor, job):
        self.sex = sex
        self.race = race
        self.level = level
        self.danger = danger
        self.attack = attack
        self.health = health
        self.armor = armor
        self.portrait = 'portraits/'
        self.job = None
        self.money = 0
        self.mana = self.max_mana
        self.speed = self.standard_speed
        self.state = self.race
        self.equipped = { 'weapon' : None,
                         'armor'  : None,
                         'boots'  : None }
        self.inventory = [ None ]
        if self.sex == 'male':
            self.name = random.choice(self.male_names)
        else:
            self.name = random.choice(self.female_names)

    def __sub__(self, other):
        # It is an attack function
        self.health -= 0.01 * (150 - 0.75 * self.armor * other.attack)
        if self.item['armor'] == None:
            self.armor  -= 0.03 * other.attack
        else:
            self.item_strength['armor'] -= random.randint(0, 4)

        if other.item['weapon'] != None:
            other.item_strength['weapon'] -= random.randint(0, 4)

    def __str__(self):
        inv = ', '.join(map(str, self.inventory))
        data = [ 'name :      ' + str(self.name),
                 'race :      ' + str(self.race),
                 'sex :       ' + str(self.sex),
                 'level :     ' + str(self.level),
                 'danger :    ' + str(self.danger),
                 'attack :    ' + str(self.attack),
                 'health :    ' + str(self.health),
                 'armor :     ' + str(self.armor),
                 'mana :      ' + str(self.mana),
                 'speed :     ' + str(self.speed),
                 'money :     ' + str(self.money),
                 'equipped :  ' + str(self.equipped),
                 'inventory : ' + inv ]

        data = '\n'.join(map(str, data))
        return data

    def set_name(self, name, speech = False):
        name = name[0].upper() + name[1:].lower()
        if speech:
            print("{} changed his name to {}!".format(self.name, name))
        self.name = name

    def levelup(self, speech = False):
        self.level += 1
        if speech:
            print("Level up! {} is now level {}!".format(self.name, self.level))

    def set_danger(self, danger, speech = False):
        if danger in dangers:
            self.danger = danger
        elif speech:
            print('Make sure you set the danger level correctly and try again please.')

    def set_stats(self, level = None, attack = None, health = None,
    armor = None, speech = False):
        if speech and self.health != None:
            print("{}\'s health was ".format(self.name), end='')
            if health - self.attack > 0:
                print("increased by {} ({}).".format(health - self.health, health))
            else:
                print("decreased by {} ({}).",format(self.health - health, health))

        if speech and self.attack != None:
            print("{}\'s attack was ".format(self.name), end='')
            if attack - self.attack > 0:
                print("increased by {} ({}).".format(attack - self.attack, attack))
            else:
                print("decreased by {} ({}).",format(self.attack - attack, attack))

        if speech and self.health != None:
            print("{}\'s health was ".format(self.name), end='')
            if health - self.attack > 0:
                print("increased by {} ({}).".format(health - self.health, health))
            else:
                print("decreased by {} ({}).",format(self.health - health, health))

        if speech and self.armor != None:
            print("{}\'s armor was ".format(self.name), end='')
            if armor - self.attack > 0:
                print("increased by {} ({}).".format(armor - self.armor, armor))
            else:
                print("decreased by {} ({}).",format(self.armor - armor, armor))

        self.attack = attack
        self.health = health
        self.armor = armor

    def set_job(self, new_job, speech = False):
        if new_job in self.jobs:
            if speech:
                print("{} was fired from job \"{}\".".format(self.name, self.job))
                print("{} got a job \"{}\".".format(self.name, new_job))
            self.job = new_job
        else:
            print("The job is incorrect")

    def ability(self):
        print("Actually, this creature {} doesn't have any ability...".format(self.name))

    def print_stats(self):
        print("{} is now level {}, ".format(self.name, self.level), end='')
        if self.sex == 'male': print("he ", end='')
        else: print("she ", end='')
        print("is {}. \n{} has {} damage, {} health and {} armor.".format(self.race,
        self.name, self.attack, self.health, self.armor))
