from creatures.creature import creature

class treant(creature):

    def __init__(self, sex, race, level, danger, attack, health, armor, job):
        creature.__init__(self, sex, race, level, danger, attack, health, armor, job)
        self.ability = 'invulnerability'
        self.race = 'human'
        self.state = self.race
        self.armor -= creature.standard
        self.attack -= creature.standard
        self.health += creature.much
        self.real_health = self.health
        self.portrait += 'treant.txt'

    def ability(self):
        # invulnerability
        if self.state == 'treant':
            self.state = 'astral'
            self.health = math.inf
            self.speed = 0
        else:
            self.state = 'treant'
            self.health = self.real_health
            self.speed = creature.standard_speed

    def info():
        print("Treant has an ability to enter a tree astral and get invulnerability")
        print("Treant has much more health, but less attack and armor")
