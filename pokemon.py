


class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.health = 100 + (level-1)*10
        self.max_health = 100 + (level-1)*10
        self.is_ko = False



    def __repr__(self):
        return "Ein {} vom Typ {}.".format(self.name, self.type)

    def lose_health(self, hit):
        self.health -= hit
        if self.health <= 0:
            self.health = 0
            self.ko()
        else:
            print("{} now has {} health.".format(self.name, self.health))

    def gain_health(self, heal):
        if self.health == 0:
            self.revive()
            self.health += (int(heal/2))
        else:
            self.health += heal
        if self.health >= self.max_health:
            self.health = self.max_health
        print("{} now has {} health.".format(self.name, self.health))

    def ko(self):
        self.is_ko = True
        if self.health != 0:
            self.health = 0
        print("{} is KO!!!".format(self.name))

    def revive(self):
        self.is_ko = False
        if self.health == 0:
            self.health = 1
        print("{} is back!!!".format(self.name))





ronnymon = Pokemon("Ronnymon", 3, "ostdeutsch")


print(ronnymon)
ronnymon.lose_health(15)

ronnymon.gain_health(5)

ronnymon.gain_health(80)

ronnymon.lose_health(130)

ronnymon.gain_health(50)
