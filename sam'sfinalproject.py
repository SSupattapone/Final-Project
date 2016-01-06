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
print(("You have selceted level {0}. GO: ").format(level))
print(" ")

#________________________________________________________


if level == str(1):
    import random

    blanks1 = ['_ _', '_ _ _']
    b1 = random.choice(blanks1)
    b1.count('_')
    print(b1)
    
    if b1 == '_ _':
        words = [data]
        ANS1 = (random.choice(data))
        while (len(ANS1) - ANS1.count(' ')) != 2:
            ANS1 = (random.choice(data))
            print(ANS1)

    elif b1 == '_ _ _':
        words = [data]
        ANS1 = (random.choice(data))
        while (len(ANS1) - ANS1.count(' ')) != 3:
            ANS1 = (random.choice(data))
            print(ANS1)

    while b1 != ANS1:
        g1 = input("Guess a letter: ")
        if str(g1) in ANS1:
            p1 = ANS1.index(g1)
            for n,c in enumerate(b1):
                if n == p1 and p1 != 0 and p1 != len(ANS1)-1:
                    print(b1[:p1]+' '+g1+b1[p1+2:])

#________________________________________________________

elif level == str(2):
    import random

    blanks2 = ['_ _ _ _', '_ _ _ _ _']
    b2 = random.choice(blanks2)
    b2.count('_')
    print(b2)
    
    if b2 == '_ _ _ _':
        words = [data]
        ANS2 = (random.choice(data))
        while (len(ANS2) - ANS2.count(' ')) != 4:
            ANS2 = (random.choice(data))

    elif b2 == '_ _ _ _ _':
        words = [data]
        ANS2 = (random.choice(data))
        while (len(ANS2) - ANS2.count(' ')) != 5:
            ANS2 = (random.choice(data))

    while b2 != ANS2:
        g2 = input("Guess a letter: ")
        if str(g2) in ANS2:
            p2 = ANS2.index(g2)
            for n,c in enumerate(b2):
                if n == p2 and p2 != 0 and p2 != len(ANS2)-1:
                    b2 = b2[:p2]+' '+g2+b2[p2+2:]
                    print(b2)
                    

#________________________________________________________

elif level == str(3):
    import random

    blanks3 = ['_ _ _ _ _ _', '_ _ _ _ _ _ _']
    b3 = random.choice(blanks3)
    b3.count('_')
    print(b3)
    
    if b3 == '_ _ _ _ _ _':
        words = [data]
        ANS3 = (random.choice(data))
        while (len(ANS3) - ANS3.count(' ')) != 6:
            ANS3 = (random.choice(data))
    
    elif b3 == '_ _ _ _ _ _ _':
        words = [data]
        ANS3 = (random.choice(data))
        while (len(ANS3) - ANS3.count(' ')) != 7:
            ANS3 = (random.choice(data))

#________________________________________________________

elif level == str(INSANE):
    import random

    blankslvlINSANE = [ ]

print(" ")


