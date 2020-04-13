


class Pokemon:

    damage = {"tr": 2, "tg": 0.5, "tp": 0.5, "rt": 1, "rg": 2, "rp": 1, "gt": 1, "gr": 2, "gp": 0.5, "pt": 0.5, "pr": 2, "pg": 2}


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

    def attack(self, pokemon):
        hits = 0
        if self.type == "tuner" and pokemon.type == "raver":
            hits = int(((self.level-1)*2+10)*self.damage["tr"])
            pokemon.lose_health(hits)
        if self.type == "tuner" and pokemon.type == "gamer":
            hits = int(((self.level-1)*2+10)*self.damage["tg"])
            pokemon.lose_health(hits)
        if self.type == "tuner" and pokemon.type == "pumper":
            hits = int(((self.level-1)*2+10)*self.damage["tp"])
            pokemon.lose_health(hits)
        if self.type == "raver" and pokemon.type == "tuner":
            hits = int(((self.level-1)*2+10)*self.damage["rt"])
            pokemon.lose_health(hits)
        if self.type == "raver" and pokemon.type == "gamer":
            hits = int(((self.level-1)*2+10)*self.damage["rg"])
            pokemon.lose_health(hits)
        if self.type == "raver" and pokemon.type == "pumper":
            hits = int(((self.level-1)*2+10)*self.damage["rp"])
            pokemon.lose_health(hits)
        if self.type == "gamer" and pokemon.type == "tuner":
            hits = int(((self.level-1)*2+10)*self.damage["gt"])
            pokemon.lose_health(hits)
        if self.type == "gamer" and pokemon.type == "raver":
            hits = int(((self.level-1)*2+10)*self.damage["gr"])
            pokemon.lose_health(hits)
        if self.type == "gamer" and pokemon.type == "pumper":
            hits = int(((self.level-1)*2+10)*self.damage["gp"])
            pokemon.lose_health(hits)
        if self.type == "pumper" and pokemon.type == "tuner":
            hits = int(((self.level-1)*2+10)*self.damage["pt"])
            pokemon.lose_health(hits)
        if self.type == "pumper" and pokemon.type == "raver":
            hits = int(((self.level-1)*2+10)*self.damage["pr"])
            pokemon.lose_health(hits)
        if self.type == "pumper" and pokemon.type == "gamer":
            hits = int(((self.level-1)*2+10)*self.damage["pg"])
            pokemon.lose_health(hits)
        if self.type == pokemon.type:
            hits = int(((self.level-1)*2+10))
            pokemon.lose_health(hits)

        print("{} dealt {} damage to {}".format(self.name, hits, pokemon.name))




ronnymon = Pokemon("Ronnymon", 3, "tuner")
mikemon = Pokemon("Mikemon", 3, "raver")
dennismon = Pokemon("Dennismon", 3, "gamer")
mirkomon = Pokemon("Mirkomon", 3, "pumper")




ronnymon.attack(mikemon)
ronnymon.attack(dennismon)
ronnymon.attack(ronnymon)
