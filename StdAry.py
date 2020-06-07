#StdAry.py
#This program works with Optimise.py

class character:
    """The character class for Standard Array"""
    #std array values: 15, 14, 13, 12, 10, 8
    def __init__(self):#initialises class variables
        self.str = 0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.primary = "none"
        self.secondary = "none"
        self.tertiary = "none"
        self.race = "N/A"


def GetAttrScores(x):
    """Assigns attribute scores based on preferences"""

    if x.primary == "str":
        x.str = 15 #allocates highest standard array number to primary preference
    elif x.primary == "dex":
        x.dex = 15
    elif x.primary == "con":
        x.con = 15
    elif x.primary == "int":
        x.int = 15
    elif x.primary == "wis":
        x.wis = 15
    elif x.primary == "cha":
        x.cha = 15

    if x.secondary == "str":
        x.str = 14 #2nd highest number for 2nd pref
    elif x.secondary == "dex":
        x.dex = 14
    elif x.secondary == "con":
        x.con = 14
    elif x.secondary == "int":
        x.int = 14
    elif x.secondary == "wis":
        x.wis = 14
    elif x.secondary == "cha":
        x.cha = 14

    if x.tertiary == "str":
        x.str = 13 #3rd highest number for 3rd pref
    elif x.tertiary == "dex":
        x.dex = 13
    elif x.tertiary == "con":
        x.con = 13
    elif x.tertiary == "int":
        x.int = 13
    elif x.tertiary == "wis":
        x.wis = 13
    elif x.tertiary == "cha":
        x.cha = 13

    return x

def AssignOtherScores(x):
    """Cleans up other attribute scores"""
    if x.str == 0:#if we haven't changed a score from it's default, we don't care about it. Change it to "X" for the time being.
        x.str = " X"
    
    if x.dex == 0:
        x.dex = " X"
    
    if x.con == 0:
        x.con = " X"

    if x.int == 0:
        x.int = " X"

    if x.wis == 0:
        x.wis = " X"

    if x.cha == 0:
        x.cha = " X"

    return x

def PrintLeftovers(x):
    if x.secondary == "none":
        print("14, 13, 12, 10, 8\n")
    elif x.tertiary == "none" and x.secondary != "none":
        print("13, 12, 10, 8\n")
    else:
        print("12, 10, 8\n")

