from creature import creature

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
        self.portrait = 'treant.txt'

    def invulnerability(self):
        if self.state == 'treant':
            self.state = 'astral'
            self.health = math.inf
            self.speed = 0
        else:
            self.state = 'treant'
            self.health = self.real_health
            self.speed = creature.standard_speed
