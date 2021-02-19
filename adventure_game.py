import time
import random

# inventory = ['dagger']

# enemies = ['dragon', 'troll', 'wicked fairie', 'gorgon']

class Enemy:

    name = str

    defense = int

    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


class Weapon:

    name = str

    strength = int

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


dragon = Enemy('dragon', 1200)
troll = Enemy('troll', 1050)
fairie = Enemy('wicked fairie', 950)
gorgon = Enemy('gorgon', 850)

enemies = [dragon, troll, fairie, gorgon]

enemy = random.choice(enemies)

dagger = Weapon('dagger', 9)
magic_sword = Weapon('magical Sword of Orgoroth', 15)


def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(1+1/2)


def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replacement)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


#intro
weapon = dagger
print_sleep("You find yourself standing in an open field, "
            "filled with grass and yellow wildflowers.")
print_sleep("Rumor has it that a " +
            enemy.name + 
            " is somewhere around here, and has been terrifying the nearby village.")
print_sleep("In front of you is a house.")
print_sleep("To your right is a dark cave.")
print_sleep("In your hand you hold your trusty (but not very effective) dagger.")


#first choice
while True:
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    first_path = input("What would you like to do?\n(Please enter 1 or 2.)\n")
    if first_path == '1':
        print_sleep("You approach the door of the house.")
        print_sleep("You are about to knock when the door opens and out steps a "
                    + enemy.name)
        print_sleep("Eep! This is the " + enemy.name + "'s house!")
        print_sleep("The " + enemy.name + " attacks you!")
        if weapon == dagger:
            print_sleep("You feel a bit under-prepared for this, what with only "
                        "having a tiny dagger.")
        enemy_encounter = input("Would you like to (1) fight or (2) run away?")
        if enemy_encounter == '1':
            attack = random.randint(80, 120) * weapon.strength
            if attack <= enemy.defense:
                print_sleep("You do your best...")
                print_sleep("but your dagger is no match for the wicked fairie.")
                print_sleep("You have been defeated!")
            else: 
                print_sleep("As the dragon moves to attack, you unsheath your new sword.")
                print_sleep("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
                print_sleep("But the dragon takes one look at your shiny new toy and runs away!")
                print_sleep("You have rid the town of the dragon. You are victorious!")
                break
        elif enemy_encounter == '2':
            break
    elif first_path == '2':
        #approach cave
        print_sleep("You peer cautiously into the cave.")
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        weapon = magic_sword
        print_sleep("You discard your silly old dagger and take the sword with you.")
        print_sleep("You walk back out to the field.")
        break