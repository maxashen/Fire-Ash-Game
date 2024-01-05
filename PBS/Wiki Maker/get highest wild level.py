highest = 0

with open("C:\\Users\\jlee4\\Documents\\Fire Ash Game on 3.3\\Game\\PBS\\encounters.txt","r") as f1:
    for line in f1:
        if "," in line:
            level = int(line[:-1].split(",")[-1])
            if level > highest and level not in [100, 60, 53, 52, 51]:
                highest = level
print(highest)
