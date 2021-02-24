import time
import random
from enemies import Enemy
from weapons import Weapon

DRAGON = Enemy('dragon', 1200)
TROLL = Enemy('troll', 1050)
FAIRE = Enemy('wicked fairie', 950)
GORGON = Enemy('gorgon', 850)

ENEMIES = [DRAGON, TROLL, FAIRE, GORGON]

DAGGER = Weapon('dagger', 9)
MAGIC_SWORD = Weapon('magical Sword of Orgoroth', 15)


def intro(enemy: Enemy):
    print_sleep("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_sleep(f"Rumor has it that a {enemy.name} is somewhere around here, and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty (but not very effective) dagger.")


def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(3/20)


def fight(enemy: Enemy, weapon: Weapon):
    attack = random.randint(80, 120) * weapon.strength
    if attack <= enemy.defense:
        print_sleep("You do your best...")
        print_sleep(f"but your {weapon.name} is no match for the {enemy.name}.")
        print_sleep("You have been defeated!")
    elif attack > enemy.defense:
        print_sleep(f"As the {enemy.name} moves to attack, you unsheath your {weapon.name}.")
        print_sleep(f"The {weapon.name} shines brightly in your hand as you brace yourself for the attack.")
        print_sleep(f"But the {enemy.name} takes one look at your shiny new toy and runs away!")
        print_sleep(f"You have rid the town of the {enemy.name}. You are victorious!")
    print_sleep("\nGAME OVER!")


def select_path(enemy: Enemy, weapon: Weapon):
    print_sleep("\nEnter 1 to knock on the door of the house.")
    print_sleep("Enter 2 to peer into the cave.")
    while True:
        path = input("What would you like to do?\n(Please enter 1 or 2.)\n")    
        if path == '1':       
            doorknock(enemy, weapon)
            break
        elif path == '2':
            cave(enemy, weapon)
            break
    

def doorknock(enemy: Enemy, weapon: Weapon):
    print_sleep("You approach the door of the house.")
    print_sleep(f"You are about to knock when the door opens and out steps a {enemy.name}")
    print_sleep(f"Eep! This is the {enemy.name}'s house!")
    print_sleep(f"The {enemy.name} attacks you!")
    meet_enemy(enemy, weapon)


def cave(enemy: Enemy, weapon: Weapon): 
    print_sleep("You peer cautiously into the cave.")
    if weapon == MAGIC_SWORD:
        print_sleep("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    else:
        weapon = find_sword(weapon)    
    print_sleep("You walk back out to the field.")
    select_path(enemy, weapon)


def find_sword(weapon: Weapon):
    if weapon != MAGIC_SWORD:
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old dagger and take the sword with you.")
        weapon = MAGIC_SWORD
    return weapon


def play_again():    
    while True:
        again = input("\nWould you like to play again? (y/n)")
        if again == 'n':
            print_sleep("Thanks for playing! See you next time.")
            break
        elif again == 'y':
            main()


def strength_check(weapon: Weapon):
    if weapon.strength < 10:
        print_sleep("You feel a bit under-prepared for this, what with only "
                    f"having a tiny {weapon.name}.")


def meet_enemy(enemy: Enemy, weapon: Weapon):
    strength_check(weapon)
    while True:
        enemy_encounter = input("\nWould you like to (1) fight or (2) run away?")
        if enemy_encounter == '1':
            fight(enemy, weapon)
            break
        elif enemy_encounter == '2':
            print_sleep("You run back into the field. Luckily, you don't seem to have been followed.")
            select_path(enemy, weapon)


def main():
    while True:
        enemy = random.choice(ENEMIES)
        weapon = DAGGER

        intro(enemy)
        select_path(enemy, weapon)
        play_again()
        break


if __name__ == '__main__':
    main()