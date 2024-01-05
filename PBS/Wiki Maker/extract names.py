with open("pokemon.txt", "r") as f1, open("names.txt", "w") as f2:
    for line in f1:
        if "Name = " in line[:7]:
            name = line[7:]
        elif "InternalName = " in line[:15]:
            f2.write(f"{line[15:-1]},{name}")
