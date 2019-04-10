from creature import creature

class human(creature):
    # human has much money on the beginning;
    # human has more armor, but little bit less attack and health;

    def __init__(self, sex, race, level, danger, attack, health, armor, job):
        creature.__init__(self, sex, race, level, danger, attack, health, armor, job)
        # print("\nbefore:\nsex : {}\nrace : {}\nlevel : {}\ndanger : {}\nattack : {}\nhealth : {}\narmor : {}\njob : {}\n\n".format(self.sex, self.race, self.level, self.danger, self.attack, self.health, self.armor, self.job))
        self.ability = None
        self.money = 1000
        self.race = 'human'
        self.state = self.race
        self.armor += creature.standard
        self.attack -= creature.little
        self.health -= creature.little
        if self.sex == 'male':
            self.portrait += 'man.txt'
        else:
            self.portrait += 'woman.txt'
        # print("\nafter:\nsex : {}\nrace : {}\nlevel : {}\ndanger : {}\nattack : {}\nhealth : {}\narmor : {}\njob : {}\nstate : {}\nability : {}\n\n".format(self.sex, self.race, self.level, self.danger, self.attack, self.health, self.armor, self.job, self.state, self.ability))
