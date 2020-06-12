#PtBy.py
#This program works with Optimise.py

class character:
    """The character class for Point Buy"""

    def __init__(self):#initialises class variables
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.pool = 27
        self.primary = "none"
        self.secondary = "none"
        self.tertiary = "none"
        self.race = "N/A"

def GetAttrScores(x):
    """Assigns attribute scores based on preferences"""
    #15, 15, 13
    if x.primary == "str":
        x.str = 15 #allocates highest standard array number to primary preference
        x.pool = x.pool - 9
    elif x.primary == "dex":
        x.dex = 15
        x.pool = x.pool - 9
    elif x.primary == "con":
        x.con = 15
        x.pool = x.pool - 9
    elif x.primary == "int":
        x.int = 15
        x.pool = x.pool - 9
    elif x.primary == "wis":
        x.wis = 15
        x.pool = x.pool - 9
    elif x.primary == "cha":
        x.cha = 15
        x.pool = x.pool - 9
    
    if x.secondary == "str":
        x.str = 15 #highest number for 2nd pref
        x.pool = x.pool - 9
    elif x.secondary == "dex":
        x.dex = 15
        x.pool = x.pool - 9
    elif x.secondary == "con":
        x.con = 15
        x.pool = x.pool - 9
    elif x.secondary == "int":
        x.int = 15
        x.pool = x.pool - 9
    elif x.secondary == "wis":
        x.wis = 15
        x.pool = x.pool - 9
    elif x.secondary == "cha":
        x.cha = 15
        x.pool = x.pool - 9
    
    if x.tertiary == "str":
        x.str = 13 #2nd highest number for 3rd pref
        x.pool = x.pool - 5
    elif x.tertiary == "dex":
        x.dex = 13
        x.pool = x.pool - 5
    elif x.tertiary == "con":
        x.con = 13
        x.pool = x.pool - 5
    elif x.tertiary == "int":
        x.int = 13
        x.pool = x.pool - 5
    elif x.tertiary == "wis":
        x.wis = 13
        x.pool = x.pool - 5
    elif x.tertiary == "cha":
        x.cha = 13
        x.pool = x.pool - 5
    
    return x    

def GetAttrScores2(x):
    """Assigns attribute scores based on preferences"""
    #15, 15, 15
    if x.primary == "str":
        x.str = 15 #allocates highest standard array number to primary preference
        x.pool = x.pool - 9
    elif x.primary == "dex":
        x.dex = 15
        x.pool = x.pool - 9
    elif x.primary == "con":
        x.con = 15
        x.pool = x.pool - 9
    elif x.primary == "int":
        x.int = 15
        x.pool = x.pool - 9
    elif x.primary == "wis":
        x.wis = 15
        x.pool = x.pool - 9
    elif x.primary == "cha":
        x.cha = 15
        x.pool = x.pool - 9
    
    if x.secondary == "str":
        x.str = 15 #highest number for 2nd pref
        x.pool = x.pool - 9
    elif x.secondary == "dex":
        x.dex = 15
        x.pool = x.pool - 9
    elif x.secondary == "con":
        x.con = 15
        x.pool = x.pool - 9
    elif x.secondary == "int":
        x.int = 15
        x.pool = x.pool - 9
    elif x.secondary == "wis":
        x.wis = 15
        x.pool = x.pool - 9
    elif x.secondary == "cha":
        x.cha = 15
        x.pool = x.pool - 9
    
    if x.tertiary == "str":
        x.str = 15 # highest number for 3rd pref
        x.pool = x.pool - 9
    elif x.tertiary == "dex":
        x.dex = 15
        x.pool = x.pool - 9
    elif x.tertiary == "con":
        x.con = 15
        x.pool = x.pool - 9
    elif x.tertiary == "int":
        x.int = 15
        x.pool = x.pool - 9
    elif x.tertiary == "wis":
        x.wis = 15
        x.pool = x.pool - 9
    elif x.tertiary == "cha":
        x.cha = 15
        x.pool = x.pool - 9
    
    return x
    
def XOtherScores(x):
    """Cleans up other attribute scores"""
    if x.str == 8:#if we haven't changed a score from it's default, we don't care about it. Change it to "X" for the time being.
        x.str = " X"
    
    if x.dex == 8:
        x.dex = " X"
    
    if x.con == 8:
        x.con = " X"

    if x.int == 8:
        x.int = " X"

    if x.wis == 8:
        x.wis = " X"

    if x.cha == 8:
        x.cha = " X"

    return x

def AssignOtherScores(x):
    """Assigns non-preffered attribute scores"""

    PrintLeftovers(x)
    awaiting = True
    
    if x.pool == 0:#if we have no points left, just assign everything we haven't touched to 8.
        awaiting = False
        index = 5

        if x.str == 0: x.str = 8
        if x.dex == 0: x.dex = 8
        if x.con == 0: x.con = 8
        if x.int == 0: x.int = 8
        if x.wis == 0: x.wis = 8
        if x.cha == 0: x.cha = 8
        

    while awaiting:
        print("Would you like to set your remaining scores evenly or unevenly?")
        even = input(":")
        even = even.lower()

        if even == "even" or even == "evenly":
            if x.secondary == "none":#a bit of bad code design here, we have to check again how many attributes they have left, but I don't want to re-write 2 functions
                leftovers = [12, 12, 12, 11, 11]#hopefully I replace this whole thing with a completely manual point-buy function at some point...
                index = 0
            elif x.tertiary == "none":
                leftovers = ["x", 11, 10, 10, 10]#the x is here because we need the arrays to be the same length, and we won't use that anyway
                index = 1
            else:
                leftovers = ["x", "x", 10, 9, 9]
                index = 2
            awaiting = False
        elif even == "uneven" or even == "unevenly":
            if x.secondary == "none":
                leftovers = [15, 15, 8, 8, 8]
                index = 0
            elif x.tertiary != "none":
                leftovers = ["x", 15, 8, 8, 8]
                index = 1
            else:
                leftovers = ["x", "x", 12, 8, 8]
                index = 2
            awaiting = False
        else:
            print("Didn\'t understand input. Please try again:")

    while index < 5:#loop until we've finished assigning, until index goes beyond the array

        print("What attribute should receive score " + str(leftovers[index]) + " ?")
        attr = input(":")
        attr = attr.lower()

        if attr == "str" or attr == "strength":
            if x.str == 0:#checking it's not allocated already
                x.str = leftovers[index]
                index = index + 1 #shift to next number
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "dex" or attr == "dexterity":
            if x.dex == 0:
                x.dex = leftovers[index]
                index = index + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "con" or attr == "consitution":
            if x.con == 0:
                x.con = leftovers[index]
                index = index + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "int" or attr == "intelligence":
            if x.int== 0:
                x.int = leftovers[index]
                index = index + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "wis" or attr == "wisdom":
            if x.wis == 0:
                x.wis = leftovers[index]
                index = index + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "cha" or attr == "charisma":
            if x.cha == 0:
                x.cha = leftovers[index]
                index = index + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        else:
            print("That doesn\'t look like an attribute. Write either the full word, or abbreviation:")

    return x

def PrintLeftovers(x):
    """Simply prints leftover scores in no particular order"""
    
    print("\nYou have " + str(x.pool) + " points left for score distribution")
    if x.pool == 0:#we went silly, all 3 attributes are 15, no more points left
        print("Your leftover scores are:  8, 8, 8\n")
    else:
        print("These can be arranged as uniformly as:")
        if x.secondary == "none": #only primary choice. We have 15
            print("12, 12, 12, 11, 11\n")
        elif x.tertiary == "none" and x.secondary != "none": #only secondary choice. We have 15, 15
            print("11, 10, 10, 10\n")
        elif x.tertiary != "none":#sensible build chosen, 15, 15, 13
            print("10, 9, 9\n")
        
        print("Or as unevenly as:")
        if x.secondary == "none": #only primary choice. We have 15
            print("15, 15, 8, 8, 8\n")
        elif x.tertiary == "none" and x.secondary != "none": #only secondary choice. We have 15, 15
            print("15, 8, 8, 8\n")
        elif x.tertiary != "none":#sensible build chosen, 15, 15, 13
            print("12, 8, 8\n")
    
        print("Or anything else in-between!\n")
