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

def XOtherScores(x):
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

def AssignOtherScores(x):
    """Assigns non-preffered attribute scores"""

    PrintLeftovers(x)

    if x.secondary == "none":#if only primary preference exists, start from the start, we have to assign all 5 attributes
        count = 0
    elif x.tertiary == "none":#if secondary preference also exists, start one in, we only have to assign 4
        count = 1
    else:#if they've picked all 3 preferences, we only have to assign 3
        count = 2
        
    while count < 5:#loop until we've finished assigning, until index goes beyond the array

        print("What attribute should receive score " + str(max(x.stats)) + " ?")
        attr = input(":")
        attr = attr.lower()

        if attr == "str" or attr == "strength":
            if x.str == 0:#checking it's not allocated already
                x.str = max(x.stats)#uses max from the stats list, similar to GetAttrScores()
                x.stats[x.stats.index(x.str)] = 0
                count = count + 1 #increases count
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "dex" or attr == "dexterity":
            if x.dex == 0:
                x.dex = max(x.stats)
                x.stats[x.stats.index(x.dex)] = 0
                count = count + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "con" or attr == "consitution":
            if x.con == 0:
                x.con = max(x.stats)
                x.stats[x.stats.index(x.con)] = 0
                count = count + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "int" or attr == "intelligence":
            if x.int == 0:
                x.int = max(x.stats)
                x.stats[x.stats.index(x.int)] = 0
                count = count + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "wis" or attr == "wisdom":
            if x.wis == 0:
                x.wis = max(x.stats)
                x.stats[x.stats.index(x.wis)] = 0
                count = count + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        elif attr == "cha" or attr == "charisma":
            if x.cha == 0:
                x.cha = max(x.stats)
                x.stats[x.stats.index(x.cha)] = 0
                count = count + 1
                print(attr + " assigned!")
            else:
                print("Attribute already assigned! Please choose another!")

        else:
            print("That doesn\'t look like an attribute. Write either the full word, or abbreviation:")

    return x

def PrintLeftovers(x):
    """Simply prints leftover scores in no particular order"""

    print("\nYour leftover attribute scores are:")
    i = 0
    while i < 6:
        if x.stats[i] != 0:
            print(str(x.stats[i]) + ",")
        i = i + 1
    print("\n")
    
