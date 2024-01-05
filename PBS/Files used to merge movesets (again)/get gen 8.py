start = True

with open("pokemon.txt", "r") as f1, open("Gen 8 info v2.txt", "w") as f2:
    for line in f1:
        if "[810]" in line:
            start = False
        elif start:
            f2.write(line)
        else:
            pass
