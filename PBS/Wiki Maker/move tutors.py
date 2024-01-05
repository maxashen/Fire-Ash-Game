with open("move tutors.txt", "r") as f8:
    for line in f8:
        move = line.split("-")[0].replace(" ", "").upper()
        print(move)
