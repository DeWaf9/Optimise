##!/usr/bin/env python
#Optimise.py

import Funcs
print("\n\n\nWelcome to Optimise.py!")
print("What method of score generation are you using?")
print("1 - Standard Array \n2 - Point Buy \n3 - Rolled \n")


awaiting = True
while awaiting:#grabs score generation method, this changes what class is imported
    genmethod = input(":")
    if genmethod == "1":
        print("Standard Array Selected!")
        awaiting = False
        import StdAry as method
    elif genmethod == "2":
        print("Point Buy Selected!")
        awaiting = False
        import PtBy as method
    elif genmethod == "3":
        print("Rolled Stats Selected!")
        awaiting = False
        import Rolld as method
    else:
        print("Didn't understand input. Try again:")

user = method.character()#creates character object

user = Funcs.GetAttrPref(user)#Asks user for attribute preferences

if genmethod == "2" and user.tertiary != "none": #Choice in point-buy: all 3 preferences = 15, or 1st, 2nd, 3rd = 15, 15, 13
    #Note that we don't bother asking if they didn't choose a tertiary preference, they're the same otherwise
    print("Seeing as you've chosen Point Buy...")
    print("How Min-Max-y are we talking?")
    print("Sensible or MAD?")
    sillyness = input(":")
    sillyness = sillyness.lower() #drops everything to lowercase for easier string comparison

    if sillyness == "sensible":
        user = method.GetAttrScores(user)#Assigns attribute scores based on preferences: 15, 15, 13
    elif sillyness == "mad":
        user = method.GetAttrScores2(user)#Assigns attribute scores based on preferences: 15, 15, 15
else:
    user = method.GetAttrScores(user)#No choice needed for other 2 methods

user = method.AssignOtherScores(user)#Assign "X" for non-preffered scores

print("Current attribute scores:")
Funcs.PrintAttr(user)#ascii art of current configuration
print("Leftover scores:")
method.PrintLeftovers(user)#Shows leftover scores

awaiting = True
print("Include Eberron content?")# includes eberron orc, changeling, warforged & dragonmarked races
while awaiting:
    eb = input(":")
    eb = eb.lower()
    if eb == "yes" or eb == "y" or eb == "yeah":
        eb = True
        awaiting = False
    elif eb == "no" or eb == "n" or eb == "nah":
        eb = False
        awaiting = False
    else:
        print("Didn\'t understand input. Please try again:")

print("Determining optimum race...")
user = Funcs.GetRace(user, eb)#Goes through dozens of if/else statements and can use Eberron races

print("Updated attribute scores:")
Funcs.PrintAttr(user)#ascii art of current configuration

print("Preparing to calculate level required for 20 score.")
awaiting = True#Figher & Rogue's get extra ASIs, it's imporant to know beforehand
print("Are you playing as a Fighter or Rogue?")

F = False
R = False
while awaiting:#grabs user's player class, and puts them in booleans
    ForR = input(":")
    ForR = ForR.lower()
    if ForR == "yes" or ForR == "y" or ForR == "yeah":
        print("Which one?")

    elif ForR == "no" or ForR == "n" or ForR == "nah":
        print("Neither class selected!")
        awaiting = False

    elif ForR == "fighter" or ForR == "f":
        print("Fighter class selected!")
        awaiting = False
        F = True

    elif ForR == "rogue" or ForR == "r" or ForR == "rouge": 
        print("Rogue class selected!")
        awaiting = False
        R = True

    else:
        print("Didn\'t understand input. Please try again:")

TimeToTwenty = Funcs.PrintTTT(user, F, R)
print("\n\nEnd of function. Press Enter to close.")
input("")

#FUTURE IMPLEMENTATION:
#suggest other races given tertiary and secondary preferences
#print other features of selected races to provide a more informed deicion
#extend point buy attribute score preference to have more freedom than: 15, 15, 15 or 15, 15, 13.
#give user choice on non-preffered attribute scores to provide full picture
#give user choice to reserve some ASI levles for feats, and skip those levels in FuncsTTT()
#create GUI
