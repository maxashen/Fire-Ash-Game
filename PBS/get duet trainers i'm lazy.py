count = 0
trainertypes = {}


with open("C:\\Users\\jlee4\\Documents\\3.4 GC\\3.4 GC\\Game\\PBS\\trainertypes.txt","r") as f2:
    for line in f2:
        if "#" in line or "SECRET" not in line:
            pass
        else:
            newline = line[:-3].split(",")
#            print(newline[1], newline[-1])
            trainertypes[newline[1]] = newline[-2]
#            print(trainertypes)

with open("C:\\Users\\jlee4\\Documents\\3.4 GC\\3.4 GC\\Game\\PBS\\trainers.txt","r") as f1:
    for line in f1:
        if "[SECRET" in line and "2" in line:
            newline = line[1:-2].split(",")
            if trainertypes[newline[0]] == "Male":
                newline.append("0")
            else:
                newline.append("1")
            newline[1] = f'"{newline[1]}"'
            newline = ",".join(newline)
            count += 1
            spaces = " " * (3 - len(str(count)))
            print(f"  {count}{spaces} => [:{newline}],")
input("Press Enter to exit.")
