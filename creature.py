import random
import sys
import math

class creature:

    sexes = ('male', 'female')
    male_names = ('Avraam', 'Ben', 'Carl', 'Dennis', 'Eagle', 'Franc')
    female_names = ('Alivia', 'Bella', 'Clara', 'Danna', 'Erica', 'Felicia')
    jobs = ('none', 'quest', 'helper', 'warrior')
    races = ('human', 'werewolf', 'treant', 'tech', 'demon')
    dangers = ('none', 'unknown', 'safe', 'unstable', 'dangerous')

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
        self.job = job
        self.speed = self.standard_speed
        self.state = self.race
        if self.sex == 'male':
            self.name = random.choice(self.male_names)
        else:
            self.name = random.choice(self.female_names)

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

    def print_stats(self):
        print("{} is now level {}, ".format(self.name, self.level), end='')
        if self.sex == 'male': print("he ", end='')
        else: print("she ", end='')
        print("is {}. \n{} has {} damage, {} health and {} armor.".format(self.race,
        self.name, self.attack, self.health, self.armor))
