##!/usr/bin/env python
#Optimise.py
#A program that lets you meta-game & min-max to your hearts content!

import Funcs
print("\n\n\nWelcome to Optimise.py!")
print("What method of score generation are you using?")
print("1 - Standard Array \n2 - Point Buy \n3 - Rolled \n")


awaiting = True
while awaiting:#grabs score generation method, this changes what class is imported
    genmethod = int(input(":"))
    if genmethod == 1:
        print("Standard Array Selected!")
        awaiting = False
        import StdAry as method
    elif genmethod == 2:
        print("Point Buy Selected!")
        awaiting = False
        import PtBy as method
    elif genmethod == 3:
        print("Rolled Stats Selected!")
        awaiting = False
        import Rolld as method
    else:
        print("Didn't understand input. Try again:")

user = method.character()#creates character object

user = Funcs.GetAttrPref(user)#Asks user for attribute preferences

if genmethod == 2 and user.tertiary != "none": #Choice in point-buy: all 3 preferences = 15, or 1st, 2nd, 3rd = 15, 15, 13
    #Note that we don't bother asking if they didn't choose a tertiary preference, they're the same otherwise
    print("Seeing as you've chosen Point Buy...")
    print("How Min-Max-y are we talking?")
    print("Sensible or MAD?")
    sillyness = input(":")
    sillyness = sillyness.lower() #drops everything to lowercase for easier string comparison

    if sillyness == "sensible":
        user = method.GetAttrScores(user)#Assigns attribute scores based on preferences: 15, 15, 13
    else:
        user = method.GetAttrScores2(user)#Assigns attribute scores based on preferences: 15, 15, 15
    

user = method.GetAttrScores(user)#No choice needed for other 2 methods

user = method.AssignOtherScores(user)#Assign "X" for non-preffered scores

print("Current attribute scores:")
Funcs.PrintAttr(user)#ascii art of current configuration

awaiting = True
print("Include Eberron content?")# includes eberron orc, changeling, warforged & dragonmarked races
while awaiting:
    eb = input(":")
    eb = eb.lower()
    if eb == "yes" or eb == "y":
        eb = True
        awaiting = False
    elif eb == "no" or eb == "n":
        eb = False
        awaiting = False
    else:
        print("Didn\'t understand input. Please try again:")

print("Determining optimum race...")
user = Funcs.GetRace(user, eb)#Goes through dozens of if/else statements and can use Eberron races

print("Updated attribute scores:")
Funcs.PrintAttr(user)#ascii art of current configuration

print("Preparing to calculate level at 20.")
awaiting = True
print("Are you playing as a Fighter or Rogue?")#Figher & Rogue's get extra ASIs, it's imporant to know beforehand

while awaiting:#grabs user's player class, and puts them in booleans
    ForR = input(":")
    ForR = ForR.lower()
    if ForR == "yes" or ForR == "y" or ForR == "yeah":
        print("Which one?")

    elif ForR == "no" or ForR == "n" or ForR == "nah":
        print("Neither class selected!")
        awaiting = False
        Funcs.PrintTTT(user)#All other classes. Get ASIs only at 4, 8, 12, 16 & 19

    elif ForR == "fighter" or ForR == "f":
        print("Fighter class selected!")
        awaiting = False
        Funcs.PrintTTTF(user)#Fighter. Gets additional ASIs at 6 & 14

    elif ForR == "rogue" or ForR == "r" or ForR == "rouge": 
        print("Rogue class selected!")
        awaiting = False
        Funcs.PrintTTTR(user)#Rogue. Gets additional ASI at 10

    else:
        print("Didn\'t understand input. Please try again:")


#suggest other races given tertiary and secondary preferences