from creature import creature

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
        self.max_health = self.health
        self.portrait += 'tech.txt'

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
