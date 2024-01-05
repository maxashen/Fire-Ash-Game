all_moves = {}
poke = ""
moves = []
moveset = {}

with open("pokemon Gen 7 moves.txt", "r") as f1:
    for line in f1:
        if "Name = " in line:
            if len(moves) > 0:
                moveset.update({level: moves})
                moves = []
                all_moves.update({
                    poke: {
                        "Moves": moveset,
                        "TutorMoves": tutor,
                        "EggMoves": egg
                        }
                    })
                moveset = {}
            #Gets name of pokémon
            poke = line[7:-1]
        elif "Moves = " in line[:8]:
            newline = line[8:].removesuffix("\n").split(",")
            level = -1
            for i in newline:
                if i.isdigit():
                    if len(moves) > 0 and int(i) != level:
                        moveset.update({level: moves})
                        moves = []
                    level = int(i)
                elif i.isdigit() == False:
                    moves.append(i)
        elif "TutorMoves = " in line[:13]:
            tutor = line[13:].removesuffix("\n").split(",")
        elif "EggMoves = " in line[:11]:
            egg = line[11:].removesuffix("\n").split(",")

moveset.update({level: moves})
all_moves.update({poke: {"Moves": moveset,
                         "TutorMoves": tutor,
                         "EggMoves": egg
                        }
                    })

with open("pokemon Gen 8 moves.txt", "r") as f2:
    for line in f2:
        if "Name = " in line:
            poke = line[7:-1]
        elif "Moves = " in line[:8]:
            newline = line[8:].removesuffix("\n").split(",")
            while len(newline) > 0:
                level = (int(newline.pop(0)),newline.pop(0))
                replaced = False
                for x, y in all_moves[poke]["Moves"].copy().items():
                    if level[1] in y:
                        if level[0] == x:
                            pass
                        elif level[0] == 0 and x != 0:
                            try:
                                if level[1] not in all_moves[poke]["Moves"][0]:
                                    all_moves[poke]["Moves"][0].append(level[1])
                            except:
                                all_moves[poke]["Moves"].update({level[0]: [level[1]]})
                        elif level[0] != 0 and x == 0:
                            try:
                                if level[1] not in all_moves[poke]["Moves"][level[0]]:
                                    all_moves[poke]["Moves"][level[0]].append(level[1])
                            except:
                                all_moves[poke]["Moves"].update({level[0]: [level[1]]})
                        elif level[0] < x:
                            y.remove(level[1])
                            try:
                                if level[1] not in all_moves[poke]["Moves"][level[0]]:
                                    all_moves[poke]["Moves"][level[0]].append(level[1])
                            except:
                                all_moves[poke]["Moves"].update({level[0]: [level[1]]}) 
                        replaced = True
                if not replaced:
                    try:
                        if level[1] not in all_moves[poke]["Moves"][level[0]]:
                            all_moves[poke]["Moves"][level[0]].append(level[1])
                    except:
                        all_moves[poke]["Moves"].update({level[0]: [level[1]]})
            all_moves[poke]["Moves"] = dict(sorted(all_moves[poke]["Moves"].items()))
        elif "TutorMoves = " in line[:13]:
            tutor = line[13:].removesuffix("\n").split(",")
            all_moves[poke]["TutorMoves"] = all_moves[poke]["TutorMoves"] + tutor
            all_moves[poke]["TutorMoves"] = [*set(all_moves[poke]["TutorMoves"])]
            all_moves[poke]["TutorMoves"].sort()
        elif "EggMoves = " in line[:11]:
            egg = line[11:].removesuffix("\n").split(",")
            all_moves[poke]["EggMoves"] = all_moves[poke]["EggMoves"] + egg
            all_moves[poke]["EggMoves"] = [*set(all_moves[poke]["EggMoves"])]
            all_moves[poke]["EggMoves"].sort()

with open("Gen 8 info v2.txt", "r") as f3, open("pokemon Gen 7+8 moves.txt", "w") as f4:
    for line in f3:
        if "Name = " in line[:8]:
            poke = line[7:-1]
            f4.write(line)
        elif "Moves = " in line[:8]:
            message = "Moves = "
            for x,y in all_moves[poke]['Moves'].items():
              for move in y:
                message = f"{message}{x},{move},"
            message = f"{message.removesuffix(',')}\n"
            f4.write(message)
        elif "TutorMoves = " in line[:13]:
            f4.write(f"TutorMoves = {','.join(all_moves[poke]['TutorMoves'])}\n")
        elif "EggMoves = " in line[:11]:
            f4.write(f"EggMoves = {','.join(all_moves[poke]['EggMoves'])}\n")
        elif "#-" in line:
            f4.write(line)
            
