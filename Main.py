##!/usr/bin/env python
#Main.py

import Funcs
#import Gui

print("\n\n\nWelcome to Optimise!")
print("What method of score generation are you using?")
print("1 - Standard Array \n2 - Point Buy \n3 - Rolled \n")


awaiting = True
while awaiting:#grabs score generation method, this changes what class is imported. Bad code design, but I'm more just shocked that it actually works
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
        print("Didn\'t understand input. Please try again:")

user = method.character()#creates character object

user = Funcs.GetAttrPref(user)#Asks user for attribute preferences

if genmethod == "2" and user.tertiary != "none": #Choice in point-buy: all 3 preferences = 15, or 1st, 2nd, 3rd = 15, 15, 13
    #Note that we don't bother asking if they didn't choose a tertiary preference, they're the same otherwise
    print("Seeing as you've chosen Point Buy...")
    print("How Min-Max-y are we talking?")
    print("Sensible or MAD?")
    awaiting = True
    while awaiting:
        sillyness = input(":")
        sillyness = sillyness.lower() #drops everything to lowercase for easier string comparison

        if sillyness == "sensible":
            user = method.GetAttrScores(user)#Assigns attribute scores based on preferences: 15, 15, 13
            awaiting = False
        elif sillyness == "mad":
            user = method.GetAttrScores2(user)#Assigns attribute scores based on preferences: 15, 15, 15
            awaiting = False
        else:
           print("Didn\'t understand input. Please try again:")
else:
    user = method.GetAttrScores(user)#No choice needed for other 2 methods


awaiting = True#Gives users choice on their non-preffered scores
print("\nWould you like to assign your other attribute scores?")
while awaiting:
    assign = input(":")
    assign = assign.lower()

    if assign == "y" or assign == "yes" or assign == "yeah":
        user = method.AssignOtherScores(user)#Launch manual assignment method
        awaiting = False
    elif assign == "n" or assign == "no" or assign == "nah":
        user = method.XOtherScores(user)#Assign generic "X"
        method.PrintLeftovers(user)
        awaiting = False
    else:
        print("Didn\'t understand input. Please try again:")

print("Current attribute scores:")
Funcs.PrintAttr(user)#ascii art of current configuration

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

print("Attribute scores after racial bonuses:")
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
#create GUI
#give user choice to reserve some ASI levels for feats, and skip those levels in FuncsTTT()
#print other features of selected races to provide a more informed decision
#extend point buy attribute score preference to choose manually
#DONE give user choice on non-preffered attribute scores to provide full picture
#DONE add MToF races
#DONE add human reccomendations