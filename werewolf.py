import creature

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
