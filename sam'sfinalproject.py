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

    blanks1 = ['_ _', '_ _ _']
    random.choice(blanks1)
    random.choice(blanks).count('_')


elif level == str(2):
    import random

    blanks2 = ['_ _ _ _', '_ _ _ _ _']
    print(random.choice(blanks2))
    
elif level == str(3):
    import random

    blanks3 = ['_ _ _ _ _ _', '_ _ _ _ _ _ _']
    print(random.choice(blanks3))
    
elif level == str(INSANE):
    import random

    blankslvlINSANE = [ ]

print(" ")


if level == str(1):
    import random

    wordslvl1 = [data]
    
    print(random.choice(data))


