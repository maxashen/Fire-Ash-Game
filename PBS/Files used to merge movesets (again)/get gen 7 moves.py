with open("pokemon Gen 7.txt", "r") as f1, open("pokemon Gen 7 moves.txt", "w") as f2:
    for line in f1:
        if "#-" in line:
            f2.write(line)
        elif "Name = " in line or "Moves = " in line:
            f2.write(line)
