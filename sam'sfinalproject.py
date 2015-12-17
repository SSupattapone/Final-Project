"""
Sam's Final Project
Author: Sam Supattapone
Credit: "Every Word Ever" website, 
Description: Hangman.

"""
with open("everywordever.txt") as f:
    data = f.readlines()
name = input("Welcome, please enter your name: ")
print(" ")
level = input(("Hello {0}, please select a level, 1, 2, 3, or INSANE: ").format(name))
print(" ")
print(("You have selceted level {0}. Here is the level {0} problem: ").format(level))
print(" ")

if level == str(1):
    import random

    blankslvl1 = ['_ _', '_ _ _']
    print(random.choice(blankslvl1))

elif level == str(2):
    import random

    blankslvl2 = ['_ _ _ _', '_ _ _ _ _']
    print(random.choice(blankslvl2))
    
elif level == str(3):
    import random

    blankslvl3 = ['_ _ _ _ _ _', '_ _ _ _ _ _ _']
    print(random.choice(blankslvl3))
    
elif level == str(INSANE):
    import random

    blankslvlINSANE = [ ]

print(" ")
print("Guess a letter! Letters