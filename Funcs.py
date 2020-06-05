#Funcs.py
#Contains some non-class based functions used in Optimise.py

def GetAttrPref(x):
    """Goes through the process of determining user's attribute preferences"""
    
    awaiting  = [True, True, True]#one awaiting variable for each preference (1st, 2nd, 3rd)
    print("Please input primary attribute:")

    while awaiting[0]:#determines primary attribute

        x.primary = input(":")
        x.primary = x.primary.lower()#drops everything to lowercase for easier string comparison

        if x.primary == "str" or x.primary == "strength":
            x.primary = "str"#sets to one value for uniformity later on
            print("Strength chosen as primary attribute!")
            awaiting[0] = False#value picked, no longer awaiting

        elif x.primary == "dex" or x.primary == "dexterity":
            x.primary = "dex"
            print("Dexterity chosen as primary attribute!")
            awaiting[0] = False

        elif x.primary == "con" or x.primary == "constitution":
            x.primary = "con"
            print("Constitution chosen as primary attribute!")
            awaiting[0] = False

        elif x.primary == "int" or x.primary == "intelligence":
            x.primary = "int"
            print("Intelligence chosen as primary attribute!")
            awaiting[0] = False

        elif x.primary == "wis" or x.primary == "wisdom":
            x.primary = "wis"
            print("Wisdom chosen as primary attribute!")
            awaiting[0] = False

        elif x.primary == "cha" or x.primary == "charisma":
            x.primary = "cha"
            print("Charisma chosen as primary attribute!")
            awaiting[0] = False

        else:
            print("That doesn\'t look like an attribute. Write either the full word, or abbreviation:")



    print("Please input secondary attribute, or type \'none\' if you have no second preference:")

    while awaiting[1]:#determines secondary attribute
    
        x.secondary = input(":")
        x.secondary = x.secondary.lower()#drops everything to lowercase for easier string comparison

        if x.secondary == "str" or x.secondary == "strength":
            x.secondary = "str"
            if x.secondary == x.primary:#Checks for duplicate preferences
                print("Duplicate preference entered! Try again!")
            else:
                print("Strength chosen as secondary attribute!")
                awaiting[1] = False

        elif x.secondary == "dex" or x.secondary == "dexterity":
            x.secondary = "dex"
            if x.secondary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Dexterity chosen as secondary attribute!")
                awaiting[1] = False

        elif x.secondary == "con" or x.secondary == "constitution":
            x.secondary = "con"
            if x.secondary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Constitution chosen as secondary attribute!")
                awaiting[1] = False

        elif x.secondary == "int" or x.secondary == "intelligence":
            x.secondary = "int"
            if x.secondary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Intelligence chosen as secondary attribute!")
                awaiting[1] = False

        elif x.secondary == "wis" or x.secondary == "wisdom":
            x.secondary = "wis"
            if x.secondary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Wisdom chosen as secondary attribute!")
                awaiting[1] = False

        elif x.secondary == "cha" or x.secondary == "charisma":
            x.secondary = "cha"
            if x.secondary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Charisma chosen as secondary attribute!")
                awaiting[1] = False

        elif x.secondary == "none":#No 2nd preference
            print("No secondary preference selected.")
            x.tertiary = "none"
            awaiting[1] = False
            awaiting[2] = False#If there's no 2nd preference, they can't have a 3rd

        else:
            print("That doesn\'t look like an attribute. Write either the full word, or abbreviation:")

    if awaiting[2]:
        print("Please input tertiary attribute, or type \'none\' if you have no third preference:")

    while awaiting[2]:#determines tertiary attribute
    
        x.tertiary = input(":")
        x.tertiary = x.tertiary.lower()

        if x.tertiary == "str" or x.tertiary == "strength":
            x.tertiary = "str"
            if x.tertiary == x.secondary or x.tertiary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Strength chosen as tertiary attribute!")
                awaiting[2] = False

        elif x.tertiary == "dex" or x.tertiary == "dexterity":
            x.tertiary = "dex"
            if x.tertiary == x.secondary or x.tertiary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Dexterity chosen as tertiary attribute!")
                awaiting[2] = False

        elif x.tertiary == "con" or x.tertiary == "constitution":
            x.tertiary = "con"
            if x.tertiary == x.secondary or x.tertiary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Constitution chosen as tertiary attribute!")
                awaiting[2] = False

        elif x.tertiary == "int" or x.tertiary == "intelligence":
            x.tertiary = "int"
            if x.tertiary == x.secondary or x.tertiary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Intelligence chosen as tertiary attribute!")
                awaiting[2] = False

        elif x.tertiary == "wis" or x.tertiary == "wisdom":
            x.tertiary = "wis"
            if x.tertiary == x.secondary or x.tertiary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Wisdom chosen as tertiary attribute!")
                awaiting[2] = False

        elif x.tertiary == "cha" or x.tertiary == "charisma":
            x.tertiary = "cha"
            if x.tertiary == x.secondary or x.tertiary == x.primary:
                print("Duplicate preference entered! Try again!")
            else:
                print("Charisma chosen as tertiary attribute!")
                awaiting[2] = False

        elif x.tertiary == "none":
            print("No tertiary preference selected.")
            awaiting[2] = False

        else:
            print("That doesn\'t look like an attribute. Write either the full word, or abbreviation:")

    return x

def PrintAttr(x):
    print("+-----------------------------------+")
    print("| STR | DEX | CON | INT | WIS | CHA |")
    print("| " + str(x.str) + "  | " + str(x.dex) + "  | " + str(x.con) + "  | " + str(x.int) + "  | " + str(x.wis) + "  | " + str(x.cha) + "  |")
    print("+-----------------------------------+")

def GetRace(x, eb):
    """Determines optimum race based on preferences"""

    if x.primary == "str":#Strength primary


        if x.secondary == "dex":
            x.race = "Bugbear or Longtooth Shifter"
            print(x.race + " chosen!")
            x.str = x.str + 2
            x.dex = x.dex + 1


        elif x.secondary == "con":
            if eb:
                x.race = "Goliath or Half-Orc or Eberron Half-Orc"
                print(x.race + " chosen!")
                x.str = x.str + 2
                x.con = x.con + 1
            else:
                x.race = "Goliath or Half-Orc"
                print(x.race + " chosen!")
                x.str = x.str + 2
                x.con = x.con + 1


        elif x.secondary == "int":
            print("No obvious choice based on secondary preference. Using tertiary to determine race...")
            if x.tertiary == "dex":
                x.race = "Bugbear or Longtooth Shifter"
                print(x.race + " chosen!")
                x.str = x.str + 2
                x.dex = x.dex + 1
            elif x.tertiary == "con":
                if eb:
                    x.race = "Goliath or Half-Orc or Eberron Half-Orc"
                    print(x.race + " chosen!")
                    x.str = x.str + 2
                    x.con = x.con + 1
                else:
                    x.race = "Goliath or Half-Orc"
                    print(x.race + " chosen!")
                    x.str = x.str + 2
                    x.con = x.con + 1
            elif x.tertiary == "wis":
                print("Still no obvious choice based on tertiary preference... Using any Str-based class.")
                x.race = "Bugbear or Longtooth Shifter or Goliath, or any Orc variant, or Dragonborn."
                x.str = x.str + 2
            elif x.tertiary == "cha":
                x.race = "Dragonborn"
                print(x.race + " chosen!")
                x.str = x.str + 2
                x.cha = x.cha + 1
            else:
                print("No tertiary choice! Using any Str-based class.")
                x.race = "Bugbear or Longtooth Shifter or Goliath, or any Orc variant, or Dragonborn."
                x.str = x.str + 2

        elif x.secondary == "wis":
            print("No obvious choice based on secondary preference. Using tertiary to determine race...")
            if x.tertiary == "dex":
                x.race = "Bugbear or Longtooth Shifter"
                print(x.race + " chosen!")
                x.str = x.str + 2
                x.dex = x.dex + 1
            elif x.tertiary == "con":
                if eb:
                    x.race = "Goliath or Half-Orc or Eberron Half-Orc"
                else:
                    x.race = "Goliath or Half-Orc"
                print(x.race + " chosen!")
                x.str = x.str + 2
                x.con = x.con + 1
            elif x.tertiary == "int":
                print("Still no obvious choice based on tertiary preference... Using any Str-based class.")
                x.race = "Bugbear or Longtooth Shifter or Goliath, or any Orc variant, or Dragonborn."
                x.str = x.str + 2
            elif x.tertiary == "cha":
                x.race = "Dragonborn"
                print(x.race + " chosen!")
                x.str = x.str + 2
                x.cha = x.cha + 1
            else:
                print("No tertiary choice! Using any Str-based class.")
                x.race = "Bugbear or Longtooth Shifter or Goliath, or any Orc variant, or Dragonborn."
                x.str = x.str + 2

        
        elif x.secondary == "cha":
            x.race = "Dragonborn"
            print(x.race + " chosen!")
            x.str = x.str + 2
            x.cha = x.cha + 1

        
        else:
            print("No secondary choice! Using any Str-based class!")
            x.race = "Bugbear or Longtooth Shifter or Goliath, or any Orc variant, or Dragonborn."
            x.str = x.str + 2

        
    elif x.primary == "dex":#Dexterity primary
        
        
        if x.secondary == "str":
            print("No obvious choice for primary & secondary preference. Using tertiary to determine race...")
            if x.tertiary == "con":
                x.race = "Sea Elf or Goblin or Stout Halfling"
                print(x.race + " chosen!")
                x.dex = x.dex + 2
                x.con = x.con + 1
            elif x.tertiary == "int":
                x.race = "High Elf or Eladrin"
                x.dex = x.dex + 2
                x.int = x.int + 1
                print(x.race + " chosen!")
            elif x.tertiary == "wis":
                if eb:
                    x.race = "Aarakocra or Wood Elf or Kenku or Halfling Mark of Healing"
                else:
                    x.race = "Aarakocra or Wood Elf or Kenku"
                x.dex = x.dex + 2
                x.wis = x.wis + 1
                print(x.race + " chosen!")
            elif x.tertiary == "cha":
                if eb:
                    x.race = "Drow or Tabaxi or Swifthide Strider or Elf Mark of Shadow or Halfling Mark of Hospitality or Lightfoot Halfing"
                else:
                    x.race = "Drow or Tabaxi or Swifthide Strider"
                print(x.race + " chosen!")
                x.dex = x.dex + 2
                x.cha = x.cha + 1
            else: 
                print("No tertiary choice! Using any Dex-based class.")
                x.race = "Tabaxi or Swifthide Strider or Any Elf or Any Halfling or Goblin or Aaracokra or Kenku"
                x.dex = x.dex + 2


        elif x.secondary == "con":
            x.race = "Sea Elf or Goblin or Stout Halfling"
            print(x.race + " chosen!")
            x.dex = x.dex + 2
            x.con = x.con + 1
        

        elif x.secondary == "int":
            x.race = "High Elf or Eladrin"
            x.dex = x.dex + 2
            x.int = x.int + 1
            print(x.race + " chosen!")


        elif x.secondary == "wis":
            if eb:
                x.race = "Aarakocra or Wood Elf or Kenku or Halfling Mark of Healing"
            else:
                x.race = "Aarakocra or Wood Elf or Kenku"
            x.dex = x.dex + 2
            x.wis = x.wis + 1
            print(x.race + " chosen!")


        elif x.secondary == "cha":
            if eb:
                x.race = "Drow or Tabaxi or Swifthide Strider or Elf Mark of Shadow or Halfling Mark of Hospitality or Lightfoot Halfing"
            else:
                x.race = "Drow or Tabaxi or Swifthide Strider"
            print(x.race + " chosen!")
            x.dex = x.dex + 2
            x.cha = x.cha + 1


        elif x.secondary == "none":#if no secondary chosen
            if eb:
                print("No secondary choice! Using Human Mark of Passage")
                x.race = "Human Mark of Passage"
                x.dex = x.dex + 2
            else:
                print("No secondary choice! Using any Dex-based class")
                x.race = "Tabaxi or Swifthide Strider or Any Elf or Any Halfling or Goblin or Aaracokra or Kenku"
                x.dex = x.dex + 2


        elif eb and x.secondary != "none": # If eberron content is enabled, and we haven't mentioned human mark of passage, do so.
            print("Also consider Human Mark of Passage!")
            x.race = x.race + " or Human Mark of Passage"


    elif x.primary == "con":#Constitution primary


        if x.secondary == "str":
            x.race = "Mountain Dwarf, or Beasthide Shifter, or Earth Genasi"
            print(x.race + " chosen!")
            x.con = x.con + 2
            x.str = x.str + 2

        
        elif x.secondary == "dex":
            x.race = "Air Genasi"
            print(x.race + " chosen!")
            x.con = x.con + 2
            x.dex = x.dex + 1


        elif x.secondary == "int":
            if eb:
                x.race = "Fire Genasi, or Hobgoblin, or Dwarf Mark of Warding"
            else:
                x.race = "Fire Genasi, or Hobgoblin"
            print(x.race + " chosen!")
            x.con = x.con + 2
            x.int = x.int + 1
                    

        elif x.secondary == "wis":
            if eb:
                x.race = "Hill Dwarf, or Water Genasi, or Lizardfolk, or Human Mark of Sentinel"
            else:
                x.race = "Hill Dwarf, or Water Genasi, or Lizardfolk"
            print(x.race + " chosen!")
            x.con = x.con + 2
            x.wis = x.wis + 1

        
        elif x.secondary == "cha":
            print("No obvious choice for primary & secondary preference. Using tertiary to determine race...")
            if x.tertiary == "str":
                x.race = "Mountain Dwarf"
                print(x.race + " chosen!")
                x.con = x.con + 2
                x.str = x.str + 2

        
            elif x.tertiary == "dex":
                x.race = "Air Genasi"
                print(x.race + " chosen!")
                x.con = x.con + 2
                x.dex = x.dex + 1


            elif x.tertiary == "int":
                if eb:
                    x.race = "Fire Genasi, or Hobgoblin, or Dwarf Mark of Warding"
                else:
                    x.race = "Fire Genasi, or Hobgoblin"
                print(x.race + " chosen!")
                x.con = x.con + 2
                x.int = x.int + 1
                    

            elif x.tertiary == "wis":
                if eb:
                    x.race = "Hill Dwarf, or Water Genasi, or Lizardfolk, or Human Mark of Sentinel"
                else:
                    x.race = "Hill Dwarf, or Water Genasi, or Lizardfolk"
                print(x.race + " chosen!")
                x.con = x.con + 2
                x.wis = x.wis + 1

        elif x.secondary == "none":#if no secondary chosen
            if eb:
                print("No secondary choice! Using Warforged")
                x.race = "Warforged"
                x.con = x.con + 2
            else:
                print("No secondary choice! Using any Con-based class")
                x.race = "Any Genasi, or Any Dwarf, or Hobgoblin, or Lizardfolk, or Beasthide Shifter"
                x.con = x.con + 2


        elif eb and x.secondary != "none": # If eberron content is enabled, and we haven't mentioned warforged, do so.
            print("Also consider Warforged!")
            x.race = x.race + " or Warforged"


    elif x.primary == "int":#Intelligence primary
        if x.secondary == "str":
            print("No obvious choice for primary & secondary preference. Using tertiary to determine race...")
            if x.tertiary == "dex":
                x.race = "Forest Gnome or Deep Gnome"
                print(x.race + " chosen!")
                x.int = x.int + 2
                x.dex = x.dex + 1

        
            elif x.tertiary == "con":
                x.race = "Rock Gnome"
                print(x.race + " chosen!")
                x.int = x.int + 2
                x.con = x.con + 1


            elif x.tertiary == "wis":
                if eb:
                    x.race = "Human Mark of Making"
                    print(x.race + " chosen!")
                    x.int = x.int + 2
                    x.wis = x.wis + 1
                else:
                    print("Still no obvious choice based on tertiary preference... Using any Int-based class.")
                    x.race = "Any Gnome"
                    x.int = x.int + 2
                    

            elif x.tertiary == "cha":
                if eb:
                    x.race = "Gnome Mark of Scribing, or Human Mark of Making"
                    print(x.race + " chosen!")
                    x.int = x.int + 2
                    x.cha = x.cha + 1
                else:
                    print("Still no obvious choice based on tertiary preference... Using any Int-based class.")
                    x.race = "Any Gnome"
                    x.int = x.int + 2
                
        
        elif x.secondary == "dex":
            x.race = "Deep Gnome, or Forest Gnome"
            print(x.race + " chosen!")
            x.int = x.int + 2
            x.dex = x.dex + 1


        elif x.secondary == "con":
            x.race = "Rock Gnome"
            print(x.race + " chosen!")
            x.int = x.int + 2
            x.con = x.con + 1
                    

        elif x.secondary == "wis":
            print("No obvious choice for primary & secondary preference. Using tertiary to determine race...")
            if x.tertiary == "dex":
                x.race = "Forest Gnome or Deep Gnome"
                print(x.race + " chosen!")
                x.int = x.int + 2
                x.dex = x.dex + 1

        
            elif x.tertiary == "con":
                x.race = "Rock Gnome"
                print(x.race + " chosen!")
                x.int = x.int + 2
                x.con = x.con + 1


            elif x.tertiary == "str":
                if eb:
                    x.race = "Human Mark of Making"
                    print(x.race + " chosen!")
                    x.int = x.int + 2
                    x.str = x.str + 1
                else:
                    print("Still no obvious choice based on tertiary preference... Using any Int-based class.")
                    x.race = "Any Gnome"
                    x.int = x.int + 2
                    

            elif x.tertiary == "cha":
                if eb:
                    x.race = "Gnome Mark of Scribing, or Human Mark of Making"
                    print(x.race + " chosen!")
                    x.int = x.int + 2
                    x.cha = x.cha + 1
                else:
                    print("Still no obvious choice based on tertiary preference... Using any Int-based class.")
                    x.race = "Any Gnome"
                    x.int = x.int + 2

        
        elif x.secondary == "cha":
            
            if eb:
                x.race = "Gnome Mark of Scribing"
                print(x.race + " chosen!")
                x.int = x.int + 2
                x.cha = x.cha + 1
            else:
                print("No obvious choice for primary & secondary preference. Using tertiary to determine race...")
                if x.tertiary == "dex":
                    x.race = "Forest Gnome or Deep Gnome"
                    print(x.race + " chosen!")
                    x.int = x.int + 2
                    x.dex = x.dex + 1

        
                elif x.tertiary == "con":
                    x.race = "Rock Gnome"
                    print(x.race + " chosen!")
                    x.int = x.int + 2
                    x.con = x.con + 1


                elif x.tertiary == "wis":
                    print("Still no obvious choice based on tertiary preference... Using any Int-based class.")
                    x.race = "Any Gnome"
                    x.int = x.int + 2
                    

                elif x.tertiary == "str":
                    print("Still no obvious choice based on tertiary preference... Using any Int-based class.")
                    x.race = "Any Gnome"
                    x.int = x.int + 2

        elif x.secondary == "none":#if no secondary chosen
            if eb:
                print("No secondary choice! Using Human Mark of Making")
                x.race = "Human Mark of Making"
                x.int = x.int + 2
            else:
                print("No secondary choice! Using any Int-based class")
                x.race = "Any Gnome"
                x.int = x.int + 2


        elif eb and x.secondary != "none": # If eberron content is enabled, and we haven't mentioned human mark of making, do so.
            print("Also consider Human Mark of Making!")
            x.race = x.race + " or Human Mark of Making"


    elif x.primary == "wis": #Wisdom Primary
        

        if x.secondary == "str":
            x.race = "Firbolg"
            print(x.race + " chosen!")
            x.wis = x.wis + 2
            x.str = x.str + 1
        
        elif x.secondary == "dex":
            x.race = "Wildhunt Shifter"
            print(x.race + " chosen!")
            x.wis = x.wis + 2
            x.dex = x.dex + 1

        elif x.secondary == "con":
            if eb:
                x.race = "Half-Orc Mark of Finding"
                print(x.race + " chosen!")
                x.wis = x.wis + 2
                x.con = x.con + 1
            else:
                print("No obvious choice for primary & secondary preference. Using tertiary to determine race...")
                if x.tertiary == "str":
                    x.race = "Firbolg"
                    print(x.race + " chosen!")
                    x.wis = x.wis + 2
                    x.str = x.str + 1

                elif x.tertiary == "dex":
                    x.race = "Wildhunt Shifter"
                    print(x.race + " chosen!")
                    x.wis = x.wis + 2
                    x.dex = x.dex + 1

                else:
                    print("Still no obvious choice based on tertiary preference... Using any Wis-based class.")
                    x.race = "Firbolg, or Wildhunt Shifter"
                    x.int = x.int + 2
        

        elif x.secondary == "int":
            if eb:
                x.race = "Half-Elf Mark of Detection or Human Mark of Handling"
                print(x.race + " chosen!")
                x.wis = x.wis + 2
                x.int = x.int + 1
            else:
                print("No obvious choice for primary & secondary preference. Using tertiary to determine race...")
                if x.tertiary == "str":
                    x.race = "Firbolg"
                    print(x.race + " chosen!")
                    x.wis = x.wis + 2
                    x.str = x.str + 1

                elif x.tertiary == "dex":
                    x.race = "Wildhunt Shifter"
                    print(x.race + " chosen!")
                    x.wis = x.wis + 2
                    x.dex = x.dex + 1

                else:
                    print("Still no obvious choice based on tertiary preference... Using any Wis-based class.")
                    x.race = "Firbolg, or Wildhunt Shifter"
                    x.int = x.int + 2

        elif x.secondary == "cha":
            if eb:
                x.race = "Kalashtar"
                print(x.race + " chosen!")
                x.wis = x.wis + 2
                x.cha = x.cha + 1
            else:
                print("No obvious choice for primary & secondary preference. Using tertiary to determine race...")
                if x.tertiary == "str":
                    x.race = "Firbolg"
                    print(x.race + " chosen!")
                    x.wis = x.wis + 2
                    x.str = x.str + 1

                elif x.tertiary == "dex":
                    x.race = "Wildhunt Shifter"
                    print(x.race + " chosen!")
                    x.wis = x.wis + 2
                    x.dex = x.dex + 1

                else:
                    print("Still no obvious choice based on tertiary preference... Using any Wis-based class.")
                    x.race = "Firbolg, or Wildhunt Shifter"
                    x.int = x.int + 2

        elif x.secondary == "none":#if no secondary chosen
            if eb:
                print("No secondary choice! Using Human Mark of Handling or Half-Elf Mark of Detection")
                x.race = "Human Mark of Making"
                x.int = x.int + 2
            else:
                print("No secondary choice! Using any Int-based class")
                x.race = "Any Gnome"
                x.int = x.int + 2


        elif eb and x.secondary != "none": # If eberron content is enabled, and we haven't mentioned human mark of making, do so.
            print("Also consider Human Mark of Making!")
            x.race = x.race + " or Human Mark of Making"


    elif x.primary == "cha": #Charisma primary

        if x.secondary == "str":
            x.race = "Falles Aasimar, or Half-Elf"
            print(x.race + " chosen!")
            x.cha = x.cha + 2
            x.str = x.str + 1


        elif x.secondary == "dex":
            if eb:
                x.race = "Half-Elf Mark of Storm, or Changeling, or Half-Elf"
                print(x.race + " chosen!")
                x.cha = x.cha + 2
                x.dex = x.dex + 1
            else:
                x.race = "Half-Elf"
                print(x.race + " chosen!")
                x.wis = x.wis + 2
                x.dex = x.dex + 1

        
        elif x.secondary == "con":
            x.race = "Scourge Aasimar, or Half-Elf"
            print(x.race + " chosen!")
            x.cha = x.cha + 2
            x.con = x.con + 1

        
        elif x.secondary == "int":
            x.race = "Tiefling, or Half-Elf, or Yuan-Ti Pureblood"
            print(x.race + " chosen!")
            x.cha = x.cha + 2
            x.int = x.int + 1

        
        elif x.secondary == "wis":
            x.race = "Protector Aassimar, or Half-Elf"
            print(x.race + " chosen!")
            x.cha = x.cha + 2
            x.wis = x.wis + 1


        elif x.secondary == "none":#if no secondary chosen
            if eb:
                print("No secondary choice! Using Changeling or Half-Elf!")
                x.race = "Changeling, or Half-Elf"
                x.cha = x.cha + 2
            else:
                print("No secondary choice! Using any Cha-based class")
                x.race = "Half-Elf, or Any Aasimar"
                x.cha = x.cha + 2


        elif eb and x.secondary != "none": # If eberron content is enabled, and we haven't mentioned changeling, do so.
            print("Also consider Changeling")
            x.race = x.race + " or Changeling"

    return x

def PrintTTT(x):
    pass

def PrintTTTF(x):
    pass

def PrintTTTR(x):
    pass

#next
