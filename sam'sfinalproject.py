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

#________________________________________________________


if level == str(1):
    import random

    blanks1 = ['_ _', '_ _ _']
    b1 = random.choice(blanks1)
    b1.count('_')
    print(b1)
    
    words = [data]
    ANS1 = (random.choice(data))

#________________________________________________________

elif level == str(2):
    import random

    blanks2 = ['_ _ _ _', '_ _ _ _ _']
    b2 = random.choice(blanks2)
    b2.count('_')
    print(b2)
    
    words = [data]
    ANS2 = (random.choice(data))
    while (len(ANS1) - ANS1.count(' ')) not in [2,3]:
        ANS2 = (random.choice(data))

#________________________________________________________

elif level == str(3):
    import random

    blanks3 = ['_ _ _ _ _ _', '_ _ _ _ _ _ _']
    b3 = random.choice(blanks3)
    b3.count('_')
    print(b3)
    
    words = [data]
    ANS3 = (random.choice(data))

#________________________________________________________

elif level == str(INSANE):
    import random

    blankslvlINSANE = [ ]

print(" ")
    


