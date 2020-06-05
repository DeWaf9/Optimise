#Rolld.py
#This program works with Optimise.py

class character:
    """The character class for Rolled Stats"""

    def __init__(self):#initialises class variables
        self.stats = [0, 0, 0, 0, 0, 0]
        print("Please input rolled stats")#I'm not using random() to generate 4D6 drop lowest. Roll your own damn scores.
        self.stats[0] = int(input(":"))
        self.stats[1] = int(input(":"))
        self.stats[2] = int(input(":"))
        self.stats[3] = int(input(":"))
        self.stats[4] = int(input(":"))
        self.stats[5] = int(input(":"))
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

        if x.primary == "str":
            x.str = max(x.stats)#allocates highest rolled number to primary preference
            x.stats[x.stats.index(x.str)] = 0#set that number to zero once it's been used so we don't re-use it
        elif x.primary == "dex":
            x.dex = max(x.stats)
            x.stats[x.stats.index(x.dex)] = 0
        elif x.primary == "con":
            x.con = max(x.stats)
            x.stats[x.stats.index(x.con)] = 0
        elif x.primary == "int":
            x.int = max(x.stats)
            x.stats[x.stats.index(x.int)] = 0
        elif x.primary == "wis":
            x.wis = max(x.stats)
            x.stats[x.stats.index(x.wis)] = 0
        elif x.primary == "cha":
            x.cha = max(x.stats)
            x.stats[x.stats.index(x.cha)] = 0
        
        if x.secondary == "str":#basically a copy paste. No need to check for preference duplicates, we did that in Funcs.GetAttrPref()
            x.str = max(x.stats)
            x.stats[x.stats.index(x.str)] = 0
        elif x.secondary == "dex":
            x.dex = max(x.stats)
            x.stats[x.stats.index(x.dex)] = 0
        elif x.secondary == "con":
            x.con = max(x.stats)
            x.stats[x.stats.index(x.con)] = 0
        elif x.secondary == "int":
            x.int = max(x.stats)
            x.stats[x.stats.index(x.int)] = 0
        elif x.secondary == "wis":
            x.wis = max(x.stats)
            x.stats[x.stats.index(x.wis)] = 0
        elif x.secondary == "cha":
            x.cha = max(x.stats)
            x.stats[x.stats.index(x.cha)] = 0
        
        if x.tertiary == "str":#Yet another copy-paste
            x.str = max(x.stats)
            x.stats[x.stats.index(x.str)] = 0
        elif x.tertiary == "dex":
            x.dex = max(x.stats)
            x.stats[x.stats.index(x.dex)] = 0
        elif x.tertiary == "con":
            x.con = max(x.stats)
            x.stats[x.stats.index(x.con)] = 0
        elif x.tertiary == "int":
            x.int = max(x.stats)
            x.stats[x.stats.index(x.int)] = 0
        elif x.tertiary == "wis":
            x.wis = max(x.stats)
            x.stats[x.stats.index(x.wis)] = 0
        elif x.tertiary == "cha":
            x.cha = max(x.stats)
            x.stats[x.stats.index(x.cha)] = 0
        
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

