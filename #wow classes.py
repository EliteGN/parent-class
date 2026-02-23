#wow classes 
class Hunter:
    def __init__(self, name, hp, ap):
        self.name = "Huntard"
        self.hp = 420
    def attack(self, dps):
        self.dps= [1]
        print(f"Damage done: {dps}")
class Warrior:
    def __init__(self, name, hp, ap):
        self.name = "Bestprotngl"
        self.hp = 333
        self.ap = 25
    def attack(self, dps):
        self.dps= [2]
        print(f"Damage done: {dps}")

class Druid:
    def __init__(self, name, hp, ap):
        self.name = "Arcane"
        self.hp = 1
        self.ap = 2
    def attack(self, dps):
        self.dps= [3]
        print(f"Damage done: {dps}")
class Druid:
    def __init__(self, name, hp, ap): 
        self.name = "Moonkid"
        self.hp = 120
        self.ap = 100
    def attack(self, dps):
        self.dps= [4]
        print(f"Damage done: {dps} - {Druid}")