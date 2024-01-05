all_abilities = {}
all_items = {}
all_moves = {}
all_names = {}
tms = []
items = ["","",""]
tutors = []
types = ""
current = {
    "FormName": "",
    "BaseStats": "",
    "Abilities": "",
    "HiddenAbility": "",
    "Types": "",
    "Moves": [],
    "TutorMoves": [],
    "EggMoves": [],
    "WildItems": ["","",""],
    "Evolutions": "",
    "EggGroups": ""
    }


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

with open("pokemonforms.txt", "r") as f4, open("pokemon forms wiki.txt", "w") as f5:
    for line in f4:
        if line[0] == "[":
            poke = all_names[line[1:line.find(",")]]
        elif "FormName = " in line[:11]:
            name = line[11:-1]
            if poke not in name:
                name = f"{name} {poke}"
            current["FormName"] = f"\n#-----------------------------------\n### {name} ###\n#-----------------------------------\n"
        elif "Type1 = " in line[:8]:
            types = line[8:-1].capitalize()
            current["Types"] = f"Types: {types}\n"
        elif "Type2 = " in line[:8]:
            current["Types"] = f"Types: {types}, {line[8:-1].capitalize()}\n"
        elif "BaseStats = " in line[:12]:
            stats = line[12:-1].split(",")
            current["BaseStats"] = f"# Base Stats #\nHP: {stats[0]}\nAtk: {stats[1]}\nDef: {stats[2]}\nSp. Atk: {stats[4]}\nSp. Def: {stats[5]}\nSpeed: {stats[3]}\n"
        elif "Abilities = " in line[:12]:
            if "," in line:
                abilities = line[12:-1].split(",")
                abilities = f"{all_abilities[abilities[0]]}, {all_abilities[abilities[1]]}"
            else:
                abilities = all_abilities[line[12:-1]]
            current["Abilities"] = abilities
        elif "HiddenAbility = " in line[:16]:
            current["HiddenAbility"] = all_abilities[line[16:-1]]
        elif "Moves = " in line[:8]:
            current["Moves"] = line[8:-1].split(",")
        elif "TutorMoves = " in line[:13]:
            current["TutorMoves"] = line[13:-1].split(",")
        elif "EggMoves = " in line[:11]:
            current["EggMoves"] = line[11:-1].split(",")
        elif "Compatibility = " in line[:16]:
            if "," in line:
                groups = line[16:-1].split(",")
                for i,group in enumerate(groups):
                    groups[i] = reformat_group(group)
                current["EggGroups"] = f"Egg Groups: {groups[0]}, {groups[1]}\n"
            else:
                group = reformat_group(line[16:-1])
                current["EggGroups"] = f"Egg Groups: {group}\n"
        elif "WildItemCommon = " in line:
            current["WildItems"][0] = line[17:-1]
        elif "WildItemUncommon = " in line:
            current["WildItems"][1] = line[19:-1]
        elif "WildItemRare = " in line:
            current["WildItems"][2] = line[15:-1]
        elif "Evolutions = " in line[:13]:
            newline = line[13:-1].split(",")
            if newline[1] == "None":
                pass
            else:
                for i in range(len(newline)):
                    if i % 3 == 1:
                        evo = all_names[newline[i-1]]
                        if newline[i] == "Level":
                            current["Evolutions"] = f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]}.\n"
                        elif newline[i] == "LevelNight":
                            current["Evolutions"] = f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]} at night (8:00pm - 4:59am).\n"
                        elif newline[i] == "LevelEvening":
                            current["Evolutions"] = f"{evo} - Obtained by levelling up {name} to at least level {newline[i+1]} during the evening (5:00pm - 7:59pm).\n"
                        elif "Item" in newline[i]:
                            item_int = newline[i+1]
                            item = all_items[item_int]
                            if item[0] in ("A", "E", "I", "O", "U"):
                                article = "an"
                            else:
                                article = "a"
                            if newline[i] == "DayHoldItem":                           
                                current["Evolutions"] = f"{evo} - Obtained by levelling up {name} while holding {article} {item} during the day (5:00am - 7:59pm).\n"
                            elif newline[i] == "Item":
                                current["Evolutions"] = f"{evo} - Obtained by using {article} {item} on {name}.\n"
                        elif newline[i] == "Happiness":
                            current["Evolutions"] = f"{evo} - Obtained by having high friendship with {name}.\n"
                        elif newline[i] == "HasMove":
                            current["Evolutions"] = f"{evo} - Obtained by having {all_moves[newline[i+1]]} on {name}.\n"
                        elif newline[i] == "DamageDone":
                            current["Evolutions"] = f"{evo} - Obtained by recieving at least {newline[i+1]} damage on {name} in battle.\n"
                        elif newline[i] == "CriticalHits":
                            current["Evolutions"] = f"{evo} - Obtained by using dealing {newline[i+1]} critical hits with {name} in 1 battle.\n"
        elif line == "#-------------------------------\n":
            #if current["FormName"] != "": print(current)
            if current["FormName"] != "":
                f5.write(current['FormName'])
            if current["Types"] != "":
                f5.write(current["Types"])
                f5.write("#-----------------------------------\n")
            if current["BaseStats"] != "":
                f5.write(current["BaseStats"])
                f5.write("#-----------------------------------\n")
            if current["Abilities"] != "":
                f5.write(f'Abilities: {current["Abilities"]}\n')
                if current["HiddenAbility"] != current["Abilities"] and current["HiddenAbility"] != "":
                    f5.write(f'Hidden Ability: {current["HiddenAbility"]}\n')
                f5.write("#-----------------------------------\n")
            if current["Moves"] != []:
                f5.write("# Moves learnt by level up #\n")
                for i in current["Moves"]:
                    if i.isdigit():
                        spaces = " " * (4 - len(i))
                        if i == "0":
                            f5.write(f"Evo. :{spaces}")
                        else:
                            f5.write(f"Lv. {i}:{spaces}")
                    elif i.isdigit() == False:
                        f5.write(f"{all_moves[i]}\n")
                f5.write("#-----------------------------------\n")
            if current["TutorMoves"] != []:
                tm = []
                tutor = []
                for i in current["TutorMoves"]:
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
            if current["EggMoves"] != []:
                f5.write("# Egg Moves #\n")
                for i in current["EggMoves"]:
                    f5.write(f"{all_moves[i]}\n")
                f5.write("#-----------------------------------\n")
            if current["EggGroups"] != "":
                f5.write(current["EggGroups"])
                f5.write("#-----------------------------------\n")
            if current["WildItems"] != ["","",""]:
                items = current["WildItems"]
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
            if current["Evolutions"] != "":
                f5.write("# Evolutions #\n")
                f5.write(current["Evolutions"])
                f5.write("#-----------------------------------\n")
            current = {
                "FormName": "",
                "Types": "",
                "BaseStats": "",
                "Abilities": "",
                "HiddenAbility": "",
                "Moves": [],
                "TutorMoves": [],
                "EggMoves": [],
                "EggGroups": "",
                "WildItems": ["","",""],
                "Evolutions": ""
                }
    if current["FormName"] != "":
        f5.write(current['FormName'])
    if current["Types"] != "":
        f5.write(current["Types"])
        f5.write("#-----------------------------------\n")
    if current["BaseStats"] != "":
        f5.write(current["BaseStats"])
        f5.write("#-----------------------------------\n")
    if current["Abilities"] != "":
        f5.write(f'Abilities: {current["Abilities"]}\n')
        if current["HiddenAbility"] != current["Abilities"] and current["HiddenAbility"] != "":
            f5.write(f'Hidden Ability: {current["HiddenAbility"]}\n')
        f5.write("#-----------------------------------\n")
    if current["Moves"] != []:
        f5.write("# Moves learnt by level up #\n")
        for i in current["Moves"]:
            if i.isdigit():
                spaces = " " * (4 - len(i))
                if i == "0":
                    f5.write(f"Evo. :{spaces}")
                else:
                    f5.write(f"Lv. {i}:{spaces}")
            elif i.isdigit() == False:
                f5.write(f"{all_moves[i]}\n")
        f5.write("#-----------------------------------\n")
    if current["TutorMoves"] != []:
        tm = []
        tutor = []
        for i in current["TutorMoves"]:
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
    if current["EggMoves"] != []:
        f5.write("# Egg Moves #\n")
        for i in current["EggMoves"]:
            f5.write(f"{all_moves[i]}\n")
        f5.write("#-----------------------------------\n")
    if current["EggGroups"] != "":
        f5.write(current["EggGroups"])
        f5.write("#-----------------------------------\n")
    if current["WildItems"] != ["","",""]:
        items = current["WildItems"]
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
    if current["Evolutions"] != "":
        f5.write("# Evolutions #\n")
        f5.write(current["Evolutions"])
        f5.write("#-----------------------------------\n")                   

            



            
