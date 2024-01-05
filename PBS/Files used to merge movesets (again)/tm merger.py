all_moves = {}
poke = ""
moves = []
moveset = {}

with open("pokemon Gen 7+8 moves.txt", "r") as f1:
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

with open("tm.txt", "r") as f2:
    for line in f2:
        if "#" in line:
            pass
        elif "[" in line:
            move = line[1:-2]
        else:
            newline = line.removesuffix("\n").split(",")
            for poke in newline:
                if poke == "NIDORANfE": poke = "Nidoranâ™€"
                elif poke == "NIDORANmA": poke = "Nidoranâ™‚"
                elif poke == "TYPENULL": poke = "Type: Null"
                elif poke == "JANGMOO": poke = "Jangmo-o"
                elif poke == "HAKAMOO": poke = "Hakamo-o"
                elif poke == "KOMMOO": poke = "Kommo-o"
                elif poke == "MRMIME": poke = "Mr. Mime"
                elif poke == "MIMEJR": poke = "Mime Jr."
                elif poke == "PORYGON2": poke = "Porygon2"
                elif poke == "PORYGONZ": poke = "Porygon-Z"
                elif poke == "FARFETCHD": poke = "Farfetch'd"
                elif poke == "HOOH": poke = "Ho-Oh"
                elif poke == "FLABEBE": poke = "FlabÃ©bÃ©"
                elif "TAPU" in poke: poke = f"{poke[:4].capitalize()} {poke[4:].capitalize()}"
                else: poke = poke.capitalize()
                if ("2" not in poke and poke != "Porygon2") and "3" not in poke and poke != "" and move not in all_moves[poke]["TutorMoves"]:
                    all_moves[poke]["TutorMoves"].append(move)

for i in all_moves:
    all_moves[i]["TutorMoves"].sort()

with open("Gen 8 info v2.txt", "r") as f3, open("pokemon moves with 2.28 TMs.txt", "w") as f4:
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
        else:
            f4.write(line)

        
