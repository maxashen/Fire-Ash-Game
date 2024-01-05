all_abilities = {}
all_items = {}
all_moves = {}
all_names = {}
tms = []
items = ["","",""]
tutors = []

with open("abilities.txt", "r") as f1:
    for line in f1:
        if "#" in line:
            pass
        elif "," in line:
            newline = line.split(",")
            all_abilities.update({newline[1]: newline[2]})

with open("moves.txt", "r") as f2:
    for line in f2:
        if "#" in line:
            pass
        elif "," in line:
            newline = line.split(",")
            all_moves.update({newline[1]: newline[2]})

with open("items.txt", "r") as f3:
    for line in f3:
        if "#" in line:
            pass
        elif "," in line:
            newline = line.split(",")
            if "TM" in newline[1][:2]:
                tms.append(newline[-2])
            all_items.update({newline[1]: newline[2]})

with open("names.txt", "r") as f6:
    for line in f6:
        newline = line[:-1].split(",")
        all_names.update({newline[0]: newline[1]})

with open("move tutors.txt", "r") as f7:
    for line in f7:
        tutor = line.split("-")[0].replace(" ", "").upper()
        tutors.append(tutor)

def reformat_group(group):
    if group[-1].isdigit():
        group = f"{group[:-1]} {group[-1]}"
    elif group == "Humanlike":
        group = "Human-Like"
    return group

stop = input("Where would you like to stop? (You can just press enter if you want to go to the end)")

with open("pokemon.txt", "r") as f4, open("pokemon wiki.txt", "w") as f5:
    for line in f4:
        if f"[{stop}]" in line or (f"Name = {stop.capitalize()}" in line and stop != ""):
            break
        elif "Name = " in line[:7]:
            name = line[7:-1]
            f5.write(f"\n#-----------------------------------\n### {name} ###\n#-----------------------------------\n")
        elif "Type1 = " in line[:8]:
            types = line[8:-1].capitalize()
        elif "Type2 = " in line[:8]:
            types = f"{types}, {line[8:-1].capitalize()}"
        elif "BaseStats = " in line[:12]:
            f5.write(f"Types: {types}\n")
            f5.write("#-----------------------------------\n")
            stats = line[12:-1].split(",")
            f5.write(f"# Base Stats #\nHP: {stats[0]}\nAtk: {stats[1]}\nDef: {stats[2]}\nSp. Atk: {stats[4]}\nSp. Def: {stats[5]}\nSpeed: {stats[3]}\n")
            f5.write("#-----------------------------------\n")
        elif "Abilities = " in line[:12]:
            if "," in line:
                abilities = line[12:-1].split(",")
                abilities = f"{all_abilities[abilities[0]]}, {all_abilities[abilities[1]]}"
            else:
                abilities = all_abilities[line[12:-1]]
            f5.write(f"Abilities: {abilities}\n")
        elif "HiddenAbility = " in line[:16]:
            f5.write(f"Hidden Ability: {all_abilities[line[16:-1]]}\n")
        elif "Moves = " in line[:8]:
            f5.write("#-----------------------------------\n")
            f5.write("# Moves learnt by level up #\n")
            newline = line[8:-1].split(",")
            for i in newline:
                if i.isdigit():
                    spaces = " " * (4 - len(i))
                    if i == "0":
                        f5.write(f"Evo. :{spaces}")
                    else:
                        f5.write(f"Lv. {i}:{spaces}")
                elif i.isdigit() == False:
                    f5.write(f"{all_moves[i]}\n")
            f5.write("#-----------------------------------\n")
        elif "TutorMoves = " in line[:13]:
            newline = line[13:-1].split(",")
            tm = []
            tutor = []
            for i in newline:
                if i in tms:
                    tm.append(i)
                if i in tutors:
                    tutor.append(i)
            if len(tm) > 0:
                f5.write("# Moves learnt by TM #\n")
                for i in tm:
                    f5.write(f"{all_moves[i]}\n")
                f5.write("#-----------------------------------\n")
            if len(tutor) > 0:
                f5.write("# Move Tutor moves #\n")
                for i in tutor:
                    f5.write(f"{all_moves[i]}\n")
                f5.write("#-----------------------------------\n")
        elif "EggMoves = " in line[:11]:
            f5.write("# Egg Moves #\n")
            newline = line[11:-1].split(",")
            for i in newline:
                f5.write(f"{all_moves[i]}\n")
            f5.write("#-----------------------------------\n")
        elif "Compatibility = " in line[:16]:
            if "," in line:
                groups = line[16:-1].split(",")
                for i,group in enumerate(groups):
                    groups[i] = reformat_group(group)
                f5.write(f"Egg Groups: {groups[0]}, {groups[1]}\n")
            else:
                group = reformat_group(line[16:-1])
                f5.write(f"Egg Groups: {group}\n")
        elif "StepsToHatch = " in line[:15]:
            if name[0] in ("A", "E", "I", "O", "U"):
                article = "an"
            else:
                article = "a"
            f5.write(f"Steps required to hatch {article} {name} egg: {line[15:-1]}\n")
        elif "Height = " in line[:9]:
            f5.write("#-----------------------------------\n")
        elif "WildItemCommon = " in line:
            items[0] = line[17:-1]
        elif "WildItemUncommon = " in line:
            items[1] = line[19:-1]
        elif "WildItemRare = " in line:
            items[2] = line[15:-1]
        elif "BattlerPlayer" in line and items != ["","",""]:
            f5.write(f"In the wild {name} can hold:\n")
            if items[0] == items[1] == items[2]:
                f5.write(f"{all_items[items[0]]} (100%)\n")
            elif items[0] == items[1] and items[0] != "":
                f5.write(f"{all_items[items[0]]} (55%)\n")
                if items[2] != "":
                    f5.write(f"{all_items[items[2]]} (1%)\n")
            elif items[0] == items[2] and items[0] != "":
                f5.write(f"{all_items[items[0]]} (51%)\n")
                if items[1] != "":
                    f5.write(f"{all_items[items[1]]} (5%)\n")
            elif items[1] == items[2] and items[1] != "":
                f5.write(f"{all_items[items[1]]} (6%)\n")
                if items[0] != "":
                    f5.write(f"{all_items[items[0]]} (50%)\n")
            else:
                if items[0] != "": f5.write(f"{all_items[items[0]]} (50%)\n")
                if items[1] != "": f5.write(f"{all_items[items[1]]} (5%)\n")
                if items[2] != "": f5.write(f"{all_items[items[2]]} (1%)\n")
            f5.write("#-----------------------------------\n")
            items = ["","",""]
        elif "Evolutions = " in line[:13]:
            newline = line[13:-1].split(",")
            if newline[1] in ("None", "ItemAlcremie", "Kubfu"):
                pass
            else:
                f5.write("# Evolutions #\n")
                writen = False
                for i in range(len(newline)):
                    if i % 3 == 1:
                        evo = all_names[newline[i-1]]
                        if newline[i] == "Level" or newline[i] == "Ninjask":
                            f5.write(f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]}.\n")
                        elif "Item" in newline[i]:
                            item_int = newline[i+1]
                            item = all_items[item_int]
                            if item[0] in ("A", "E", "I", "O", "U"):
                                article = "an"
                            else:
                                article = "a"
                            if newline[i] == "DayHoldItem":                                    
                                f5.write(f"{evo} - Obtained by levelling up {name} while holding {article} {item} during the day (5:00am - 7:59pm).\n")
                            elif newline[i] == "NightHoldItem":
                                f5.write(f"{evo} - Obtained by levelling up {name} while holding {article} {item} at night (8:00pm - 4:59am).\n")
                            elif newline[i] == "ItemMale":
                                f5.write(f"{evo} - Obtained by using {article} {item} on a male {name}.\n")
                            elif newline[i] == "ItemFemale":
                                f5.write(f"{evo} - Obtained by using {article} {item} on a female {name}.\n")
                            elif newline[i] == "HoldItem":
                                f5.write(f"{evo} - Obtained by levelling up {name} while holding {article} {item}.\n")
                            elif newline[i] == "Item":
                                f5.write(f"{evo} - Obtained by using {article} {item} on {name}.\n")
                        elif newline[i] == "Happiness":
                            f5.write(f"{evo} - Obtained by having high friendship with {name}.\n")
                        elif newline[i] == "Location":
                            if newline[i+1] == "393":
                                condition = "in a magnetic field"
                            elif newline[i+1] == "371":
                                condition = "near a Mossy Rock"
                            elif newline[i+1] == "622":
                                condition = "near a Icy Rock"
                            if writen == False:
                                f5.write(f"{evo} - Obtained by levelling up {name} {condition}.\n")
                                writen = True
                        elif newline[i] == "HasMove":
                            f5.write(f"{evo} - Obtained by having {all_moves[newline[i+1]]} on {name}.\n")
                        elif newline[i] == "HappinessMoveType":
                            f5.write(f"{evo} - Obtained by having max friendship with {name} while it has a {newline[i+1].capitalize()} type move.\n")
                        elif newline[i] == "HappinessDay":
                            f5.write(f"{evo} - Obtained by having high friendship with {name} during the day (5:00am - 7:59pm).\n")
                        elif newline[i] == "HappinessNight":
                            f5.write(f"{evo} - Obtained by having high friendship with {name} at night (8:00pm - 4:59am).\n")
                        elif newline[i] == "AttackGreater":
                            f5.write(f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]} while its attack stat is greater than its defense stat.\n")
                        elif newline[i] == "DefenseGreater":
                            f5.write(f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]} while its defense stat is greater than its attack stat.\n")
                        elif newline[i] == "AtkDefEqual":
                            f5.write(f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]} while its attack stat is equal than its defense stat.\n")
                        elif newline[i] == "Silcoon" or newline[i] == "Cascoon":
                            f5.write(f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]}, randomly based on personality.\n")
                        elif newline[i] == "Shedinja":
                            f5.write(f"{evo} - Obtained by having an empty slot in your party and a Poké Ball in your bag.\n")
                        elif newline[i] == "LevelFemale":
                            f5.write(f"{evo} - Obtained by levelling up a female {name} to at least level {newline[i+1]}.\n")
                        elif newline[i] == "LevelMale":
                            f5.write(f"{evo} - Obtained by levelling up a male {name} to at least level {newline[i+1]}.\n")
                        elif newline[i] == "HasInParty":
                            f5.write(f"{evo} - Obtained by levelling up {name} while {all_names[newline[i+1]]} is in the party.\n")
                        elif newline[i] == "LevelDarkInParty":
                            f5.write(f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]} with a Dark type Pokémon in your party.\n")
                        elif newline[i] == "LevelDay":
                            f5.write(f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]} during the day (5:00am - 7:59pm).\n")
                        elif newline[i] == "LevelNight":
                            f5.write(f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]} at night (8:00pm - 4:59am).\n")
                f5.write("#-----------------------------------\n")

            
                    


            
