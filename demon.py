from creature import creature

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
