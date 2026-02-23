#parent class
class Character:
    def __init__(self, name, hp, ap): 
        self.name = name
        self.hp = hp
        self.ap = ap
class Warrior(Character):
    def attack(self):
        print(f"{self.name} uses bash for {self.ap} damage")
w = Warrior("Dis",100, 6)
print("Warrior name is", w.name)
w.attack()
class Druid(Character):
    def attack(self):
        print(f"{self.name} uses swipe for {self.ap} damage")
d = Druid("Beer", 100, 7)
print("Druids name is", d.name)
d.attack()
class Mage(Character):
    def attack(self):
        print(f"{self.name} uses frost bolt for {self.ap} damage")
m = Mage("Airstrike", 100, 8)
print("Mage name is", d.name)
m.attack()
class Hunter(Character):
    def attack(self):
        print(f"{self.name} uses arcane shot for {self.ap} damage")
h = Hunter("Wallhacker", 100, 9)
print("Hunter name is", d.name)
h.attack()