"""
with open("items.txt", "r") as f1:
    for line in f1:
        if "#" in line:
            pass
        elif "," in line:
            newline = line.split(",")
            all_items.update({newline[2]: newline[1]})
"""

items = {}

with open("Thief guide.txt", "r") as f2:
    for line in f2:
        if "#" in line:
            try:
                temp = items[item]
                items[item].update({name: percent})
            except KeyError:
                items.update({item: {name: percent}})
        elif "%" in line:
            pos = line.find("(")
            item = line[:pos]
            percent = line[pos:-1]
        else:
            name = line[:-1]

with open("sorted items.txt", "w") as f3:
    f3.write("#-------------------------------\n")
    for item in items:
        f3.write(f"{item}\n")
        for name,percent in items[item].items():
            f3.write(f"{name} {percent}\n")
        f3.write("#-------------------------------\n")

