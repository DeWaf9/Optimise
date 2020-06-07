#PtBy.py
#This program works with Optimise.py

class character:
    """The character class for Point Buy"""

    def __init__(self):#initialises class variables
        self.str = 8
        self.dex = 8
        self.con = 8
        self.int = 8
        self.wis = 8
        self.cha = 8
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
    
def AssignOtherScores(x):
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

def PrintLeftovers(x):
    """Simply prints leftover scores in no particular order"""
    
    print("You have " + str(x.pool) + " points left for score distribution")
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


