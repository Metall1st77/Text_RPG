import random
import sys
import math

max_level  = 100
max_attack = 100
max_health = 100
max_armor = 100

sexes = ('male', 'female')
male_names = ('Avraam', 'Ben', 'Carl', 'Dennis', 'Eagle', 'Franc')
female_names = ('Alivia', 'Bella', 'Clara', 'Danna', 'Erica', 'Felicia')
jobs = ('none', 'quest', 'helper', 'warrior')
races = ('human', 'werewolf', 'treant', 'tech', 'demon')
dangers = ('none', 'unknown', 'safe', 'unstable', 'dangerous')

job_for_race = {'human' : 'trader',
                'werewolf' : 'hunter',
                'treant' : 'forester',
                'tech' : 'engineer',
                'demon' : 'devourer'}

interferences = ('@', '#', '$', '%', '&', '*')

class creature:

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
            self.name = random.choice(male_names)
        else:
            self.name = random.choice(female_names)

    def set_name(self, name, speech = False):
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
        if new_job in jobs:
            if speech:
                print("{} was fired from job \"{}\".".format(self.name, self.job))
                print("{} got a job \"{}\".".format(self.name, new_job))
            self.job = job
        else:
            print("The job is incorrect")

    def print_stats(self):
        print("{} is now level {}, ".format(self.name, self.level), end='')
        if self.sex == 'male': print("he ", end='')
        else: print("she ", end='')
        print("is {}. \n{} has {} damage, {} health and {} armor.".format(self.race,
        self.name, self.attack, self.health, self.armor))

class human(creature):
    # human has an ability to talk with all other races without any problems;
    # human has more armor, but little bit less attack and health;

    def __init__(self, sex, race, level, danger, attack, health, armor, job):
        creature.__init__(self, sex, race, level, danger, attack, health, armor, job)
        # print("\nbefore:\nsex : {}\nrace : {}\nlevel : {}\ndanger : {}\nattack : {}\nhealth : {}\narmor : {}\njob : {}\n\n".format(self.sex, self.race, self.level, self.danger, self.attack, self.health, self.armor, self.job))
        self.ability = 'translation'
        self.race = 'human'
        self.state = self.race
        self.armor += creature.standard
        self.attack -= creature.little
        self.health -= creature.little
        # print("\nafter:\nsex : {}\nrace : {}\nlevel : {}\ndanger : {}\nattack : {}\nhealth : {}\narmor : {}\njob : {}\nstate : {}\nability : {}\n\n".format(self.sex, self.race, self.level, self.danger, self.attack, self.health, self.armor, self.job, self.state, self.ability))

class werewolf(creature):
    # werewolf has an ability to become either human or wolf;
    # as wolf he is faster and has more attack and health, but less armor,
    # as human he is slower and has more armor, but less attack and health;

    def __init__(self, sex, race, level, danger, attack, health, armor, job):
        creature.__init__(self, sex, race, level, danger, attack, health, armor, job)
        self.ability = 'transformation'
        self.race = 'human'
        self.state = self.race
        self.armor += creature.standard
        self.attack -= creature.little
        self.health -= creature.little

    def transform(self, speech):
        if self.state == 'human':
            self.state = 'wolf'
            self.armor -= 2 * creature.standard
            self.attack += 2 * creature.little
            self.health += 2 * creature.little
            self.speed = creature.standard_speed
        else:
            self.state = 'human'
            self.armor += 2 * creature.standard
            self.attack -= 2 * creature.little
            self.health -= 2 * creature.little
            self.speed += creature.standard

class treant(creature):
    # treant has an ability to enter a tree astral and get invulnerability
    # treant has much more health, but less attack and armor

    def __init__(self, sex, race, level, danger, attack, health, armor, job):
        creature.__init__(self, sex, race, level, danger, attack, health, armor, job)
        self.ability = 'invulnerability'
        self.race = 'human'
        self.state = self.race
        self.armor -= creature.standard
        self.attack -= creature.standard
        self.health += creature.much
        self.real_health = self.health

    def invulnerability(self):
        if self.state == 'treant':
            self.state = 'astral'
            self.health = math.inf
            self.speed = 0
        else:
            self.state = 'treant'
            self.health = self.real_health
            self.speed = creature.standard_speed

class tech(creature):
    # tech has an ability to create mechanisms and restore an armor
    # tech has much more armour but much less attack

    max_mana = 100

    def __init__(self, sex, race, level, danger, attack, health, armor, job):
        creature.__init__(self, sex, race, level, danger, attack, health, armor, job)
        self.ability = 'restore'
        self.race = 'human'
        self.state = self.race
        self.armor += creature.much
        self.attack -= creature.standard
        self.health -= creature.standard
        self.mana = max_mana
        self.max_health = self.health

    def restore(self, hp):
        hp_ = hp
        for i in range(0, hp):
            if mana <= 0:
                print("{} is out of mana!".format(self.name))
                break
            if self.health >= self.max_health:
                hp_ -= hp
                break
            self.mana -= 1
            self.health += 1
            sleep(100)
        print("{}\'s {} health was restored.".format(self.name, hp_))

class demon(creature):
    # demon has an ability to eat souls
    # demon has much more attack, but less armor and health

    def __init__(self, sex, race, level, danger, attack, health, armor, job):
        creature.__init__(self, sex, race, level, danger, attack, health, armor, job)
        self.ability = 'devour'
        self.race = 'human'
        self.state = self.race
        self.armor -= creature.standard
        self.attack -= creature.standard
        self.health += creature.much
        self.souls = 0

    def devour(self):
        if self.souls <= 10:
            self.souls += 1
            print("{} got a new soul! ({} souls now)".format(self.name, self.souls))
            self.attack += creature.damage_by_soul
            print("{} now got {} damage.".format(self.name, self.attack))
        else:
            print("{} got maximum amount of souls! ({}).".format(self.name, self.souls))

if __name__ == "__main__":
    # creating a mob needs (sex, level, danger lvl, attack, health, armor, job)
    sex = 'male'
    race = 'human'
    level = 1
    danger = 'none'
    attack = 30
    health = 100
    armor = 30
    job = 'none'

    mob = creature(sex, race, level, danger, attack, health, armor, job)
    mob.set_name('George', True)
    mob.levelup(True)
    mob.set_job('helper', True)

    print()

    man = human(sex, race, level, danger, attack, health, armor, job)
    man.levelup(True)
    man.print_stats()
