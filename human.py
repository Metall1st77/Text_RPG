import creature

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
