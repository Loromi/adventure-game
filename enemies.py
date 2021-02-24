class Enemy:
    name = str
    defense = int

    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


DRAGON = Enemy('dragon', 1200)
TROLL = Enemy('troll', 1050)
FAIRE = Enemy('wicked fairie', 950)
GORGON = Enemy('gorgon', 850)

ENEMIES = [DRAGON, TROLL, FAIRE, GORGON]