


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
        print("{} is K.O.!!!".format(self.name))

    def revive(self):
        self.is_ko = False
        if self.health == 0:
            self.health = 1
        print("{} is back!!!".format(self.name))

    def attack(self, pokemon):
        hits = 0
        multi = 0
        if self.is_ko == True:
            print(self.name + " can't attack because it is K.O.!")
            return
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

class Trainer:
    def __init__(self, name, pokemon_lst, potions, active_pokemon):
        self.name = name
        self.pokemon_lst = pokemon_lst
        self.potions = potions
        self.active_pokemon = active_pokemon

    def __repr__(self):
        return "Trainer " + self.name + "!"

    def use_potion(self, amount):
        #if self.potions == 0:
        #    print("Can't heal! " + self.name + " is out of potions!")
        #    return
        #if amount > self.potions:
        #    print(self.name + " doesn't have enough potions")
        #    return
        # self.potions -= amount

        if amount == 1:
            print("{} wants to use one potion on {}".format(self.name, self.pokemon_lst[self.active_pokemon].name))
        if amount > 1:
            print("{} wants to use {} potions on {}".format(self.name, amount, self.pokemon_lst[self.active_pokemon].name))
        #if self.potions == 0:
        #    print(self.name + " is out of Potions now!")
        for i in list(range(amount)):
            if self.potions == 0:
                print("Can't heal anymore! " + self.name + " is out of potions!")
                break
            self.potions -= 1
            self.pokemon_lst[self.active_pokemon].gain_health(50)



        #while self.potions >= 1:
        #    self.potions -= 1
        #    self.pokemon_lst[self.active_pokemon].gain_health(50)


    def attack(self, trainer):
        print("{} attacked {} with his {} level {}".format(self.name, trainer.name, self.pokemon_lst[self.active_pokemon].name, self.pokemon_lst[self.active_pokemon].level))
        self.pokemon_lst[self.active_pokemon].attack(trainer.pokemon_lst[trainer.active_pokemon])

    def switch(self, pokemon_index):
        if self.pokemon_lst[pokemon_index].is_ko == True:
            print("Can't change to {} because it's K.O.!".format(self.pokemon_lst[pokemon_index].name))
            return
        self.active_pokemon = pokemon_index
        print("{} switched to {} level {}".format(self.name, self.pokemon_lst[self.active_pokemon].name, self.pokemon_lst[self.active_pokemon].level))






ronnymon_1 = Pokemon("Ronnymon", 3, "tuner")
ronnymon_2 = Pokemon("Ronnymon", 5, "tuner")
ronnymon_3 = Pokemon("Ronnymon", 6, "tuner")
mikemon_1 = Pokemon("Mikemon", 2, "raver")
mikemon_2 = Pokemon("Mikemon", 5, "raver")
mikemon_3 = Pokemon("Mikemon", 7, "raver")
dennismon_1 = Pokemon("Dennismon", 1, "gamer")
dennismon_2 = Pokemon("Dennismon", 6, "gamer")
dennismon_3 = Pokemon("Dennismon", 11, "gamer")
mirkomon_1 = Pokemon("Mirkomon", 4, "pumper")
mirkomon_2 = Pokemon("Mirkomon", 5, "pumper")
mirkomon_3 = Pokemon("Mirkomon", 6, "pumper")

rollo = Trainer("Rollo", [ronnymon_1, ronnymon_2, mikemon_2], 0, 2)
jochen = Trainer("Jochen", [ronnymon_3, mikemon_1, mirkomon_2], 2, 2)


jochen.attack(rollo)
jochen.attack(rollo)
jochen.attack(rollo)
jochen.attack(rollo)
rollo.switch(0)
rollo.switch(2)
print(rollo.active_pokemon)


#ronnymon.attack(mikemon)
#ronnymon.attack(dennismon)
#ronnymon.attack(ronnymon)
