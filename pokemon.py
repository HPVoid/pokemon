


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
        multi = 0
        if self.type == "tuner" and pokemon.type == "raver":
            multi = self.damage["tr"]
        if self.type == "tuner" and pokemon.type == "gamer":
            multi = self.damage["tg"]
        if self.type == "tuner" and pokemon.type == "pumper":
            multi = self.damage["tp"]
        if self.type == "raver" and pokemon.type == "tuner":
            multi = self.damage["rt"]
        if self.type == "raver" and pokemon.type == "gamer":
            multi = self.damage["rg"]
        if self.type == "raver" and pokemon.type == "pumper":
            multi = self.damage["rp"]
        if self.type == "gamer" and pokemon.type == "tuner":
            multi = self.damage["gt"]
        if self.type == "gamer" and pokemon.type == "raver":
            multi = self.damage["gr"]
        if self.type == "gamer" and pokemon.type == "pumper":
            multi = self.damage["gp"]
        if self.type == "pumper" and pokemon.type == "tuner":
            multi = self.damage["pt"]
        if self.type == "pumper" and pokemon.type == "raver":
            multi = self.damage["pr"]
        if self.type == "pumper" and pokemon.type == "gamer":
            multi = self.damage["pg"]
        if self.type == pokemon.type:
            multi = 1

        hits = int(((self.level-1)*2+10)*multi)

        print("{} dealt {} damage to {}".format(self.name, hits, pokemon.name))
        if multi > 1:
            print("It's super effective!")
        if multi < 1:
            print("It's not very effective!")

        pokemon.lose_health(hits)




ronnymon = Pokemon("Ronnymon", 3, "tuner")
mikemon = Pokemon("Mikemon", 3, "raver")
dennismon = Pokemon("Dennismon", 3, "gamer")
mirkomon = Pokemon("Mirkomon", 3, "pumper")




ronnymon.attack(mikemon)
ronnymon.attack(dennismon)
ronnymon.attack(ronnymon)
