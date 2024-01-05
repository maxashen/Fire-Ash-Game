backs = []

with open("metadata_Edits.txt", "r") as f1, open("metadata_condensed.txt","w") as f2:
    for line in f1:
        if "[" in line:
            f2.write(line)
        elif "BattleBack" in line:
            back = line[13:-1]
            if back not in backs:
                backs.append(back)
            f2.write(line)

print(backs)
