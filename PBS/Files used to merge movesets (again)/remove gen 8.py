stop = False

with open("pokemon Gen 8.txt", "r") as f1, open("pokemon Gen 8 moves.txt", "w") as f2:
    for line in f1:
        if "[MELMETAL]" in line:
            stop = True
        elif "#-" in line:
            f2.write(line)
            if stop:
                break
        elif "Name = " in line or "Moves = " in line:
            f2.write(line)
