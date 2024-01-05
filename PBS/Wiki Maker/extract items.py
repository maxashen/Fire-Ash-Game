all_items = {}
all_names = {}
items = ["","",""]

with open("items.txt", "r") as f1:
    for line in f1:
        if "#" in line:
            pass
        elif "," in line:
            newline = line.split(",")
            all_items.update({newline[1]: newline[2]})

with open("names.txt", "r") as f2:
    for line in f2:
        newline = line[:-1].split(",")
        all_names.update({newline[0]: newline[1]})

with open("pokemon.txt", "r") as f3, open("Thief guide.txt", "w") as f4:
    f4.write("#-----------------------------------\n")
    for line in f3:
        if "Name = " in line[:7]:
            name = line[7:-1]
        elif "WildItemCommon = " in line:
            items[0] = line[17:-1]
        elif "WildItemUncommon = " in line:
            items[1] = line[19:-1]
        elif "WildItemRare = " in line:
            items[2] = line[15:-1]
        elif "BattlerPlayerX = " in line and items != ["","",""]:
            f4.write(f"{name}\n")
            if items[0] == items[1] == items[2]:
                f4.write(f"{all_items[items[0]]} (100%)\n")
            elif items[0] == items[1] and items[0] != "":
                f4.write(f"{all_items[items[0]]} (55%)\n")
                if items[2] != "":
                    f4.write(f"{all_items[items[2]]} (1%)\n")
            elif items[0] == items[2] and items[0] != "":
                f4.write(f"{all_items[items[0]]} (51%)\n")
                if items[1] != "":
                    f4.write(f"{all_items[items[1]]} (5%)\n")
            elif items[1] == items[2] and items[1] != "":
                f4.write(f"{all_items[items[1]]} (6%)\n")
                if items[0] != "":
                    f4.write(f"{all_items[items[0]]} (50%)\n")
            else:
                if items[0] != "": f4.write(f"{all_items[items[0]]} (50%)\n")
                if items[1] != "": f4.write(f"{all_items[items[1]]} (5%)\n")
                if items[2] != "": f4.write(f"{all_items[items[2]]} (1%)\n")
            f4.write("#-----------------------------------\n")
            items = ["","",""]
