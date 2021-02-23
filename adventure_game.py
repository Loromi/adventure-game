import time
import random


class Enemy:

    name = str

    defense = int

    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


dragon = Enemy('dragon', 1200)
troll = Enemy('troll', 1050)
fairie = Enemy('wicked fairie', 950)
gorgon = Enemy('gorgon', 850)

enemies = [dragon, troll, fairie, gorgon]

enemy = random.choice(enemies)


class Weapon:

    name = str

    strength = int

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


dagger = Weapon('dagger', 9)
magic_sword = Weapon('magical Sword of Orgoroth', 15)

weapon = dagger


def intro():
    # enemy = random.choice(enemies)
    # weapon = dagger
    print_sleep("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_sleep("Rumor has it that a " +
                enemy.name + 
                " is somewhere around here, and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty (but not very effective) dagger.\n")


def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(1/20)


def fight(weapon: Weapon):
    attack = random.randint(80, 120) * weapon.strength
    print(str(attack))
    if attack <= enemy.defense:
        print_sleep("You do your best...")
        print_sleep(f"but your {weapon.name} is no match for the {enemy.name}.")
        print_sleep("You have been defeated!")
    elif attack > enemy.defense:
        print_sleep(f"As the {enemy.name} moves to attack, you unsheath your {weapon.name}.")
        print_sleep(f"The {weapon.name} shines brightly in your hand as you brace yourself for the attack.")
        print_sleep(f"But the {enemy.name} takes one look at your shiny new toy and runs away!")
        print_sleep(f"You have rid the town of the {enemy.name}. You are victorious!")
    else:
        play_again()


def select_path(weapon: Weapon):
    print_sleep("Enter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    path = input("What would you like to do?\n(Please enter 1 or 2.)\n")    
    if path == '1':       
        doorknock()
    elif path == '2':
        cave(weapon)
    else:    
        select_path(weapon)


def doorknock():
    print_sleep("You approach the door of the house.")
    print_sleep("You are about to knock when the door opens and out steps a "
                + enemy.name)
    print_sleep("Eep! This is the " + enemy.name + "'s house!")
    print_sleep("The " + enemy.name + " attacks you!")
    meet_enemy(weapon)


def cave(weapon: Weapon):    
    print_sleep("You peer cautiously into the cave.")
    if weapon != magic_sword:
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old dagger and take the sword with you.")
        weapon = magic_sword
        # return weapon
    else:
        print_sleep("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    print_sleep("You walk back out to the field.")
    select_path(weapon)


def play_again():    
    again = input("Would you like to play again? (y/n)")
    if again == 'n':
        print_sleep("Thanks for playing! See you next time.")
    elif again == 'y':
        main(weapon, enemy)
    else:    
        play_again() 


def strength_check(weapon: Weapon):
    if weapon.strength < 10:
        print_sleep("You feel a bit under-prepared for this, what with only "
                    f"having a tiny {weapon.name}.")


def meet_enemy(weapon: Weapon):
    strength_check(weapon)
    enemy_encounter = input("Would you like to (1) fight or (2) run away?")
    if enemy_encounter == '1':
        fight(weapon)
    elif enemy_encounter == '2':
        print_sleep("You run back into the field. Luckily, you don't seem to have been followed.")
        select_path(weapon)
    else:    
        meet_enemy(weapon)


def main(enemy: Enemy, weapon: Weapon):
    # enemy = random.choice(enemies)
    # weapon = dagger
    intro()
    select_path(weapon)
    play_again()


main(enemy, weapon)
           
