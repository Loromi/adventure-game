class Weapon:
    name = str
    strength = int

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


DAGGER = Weapon('dagger', 9)
MAGIC_SWORD = Weapon('magical Sword of Orgoroth', 15)