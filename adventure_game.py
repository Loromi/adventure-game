import time
import random

inventory = ['dagger']

enemies = ['dragon', 'troll', 'wicked fairie', 'gorgon']

def print_sleep(message_to_print):
    print(message_to_print)
    time.sleep(1+1/2)

#intro
print_sleep("You find yourself standing in an open field, "
            "filled with grass and yellow wildflowers.")
print_sleep("Rumor has it that a " +
            random.choice(enemies) + 
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
        #approach house
        break
    elif first_path == '2':
        #approach cave
        break