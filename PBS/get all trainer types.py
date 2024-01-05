with open("trainertypes.txt", "r") as f1:
    for line in f1:
        if "#" in line:
            pass
        else:
            print(line.split(',')[1])
