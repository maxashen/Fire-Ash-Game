moves = {
  "Bulbasaur": {
    "Moves": {
      1: ["TACKLE", "GROWL"],
      3: ["VINEWHIP"],
      6: ["GROWTH"]
    },
    "TutorMoves": ["AMNESIA", "ATTRACT"],
    "EggMoves": ["AMNESIA", "CHARM"]
  }
}

#print(moves)

#level = moves["Bulbasaur"]["Moves"]
#print(level)

newlevel = 4
move = "GROWTH"
level = (newlevel, move)
for x, y in all_moves[poke]["Moves"].copy().items():
    if level[1] in y:
        if level[0] == x:
            pass
        elif level[0] == 0 and x != 0:
            try:
                if level[1] not in all_moves[poke]["Moves"][0]:
                    moves["Bulbasaur"]["Moves"][0].append(level[1])
            except:
                moves["Bulbasaur"]["Moves"].update({level[0]: [level[1]]})
        elif level[0] != 0 and x == 0:
            try:
                if level[1] not in moves["Bulbasaur"]["Moves"][level[0]]:
                    moves["Bulbasaur"]["Moves"][level[0]].append(level[1])
            except:
                moves["Bulbasaur"]["Moves"].update({level[0]: [level[1]]})
        elif level[0] < x:
            y.remove(level[1])
            try:
                if level[1] not in moves["Bulbasaur"]["Moves"][level[0]]:
                    moves["Bulbasaur"]["Moves"][level[0]].append(level[1])
            except:
                moves["Bulbasaur"]["Moves"].update({level[0]: [level[1]]}) 
        replaced = True
if not replaced:
    try:
        if level[1] not in moves["Bulbasaur"]["Moves"][level[0]]:
            moves["Bulbasaur"]["Moves"][level[0]].append(level[1])
    except:
        moves["Bulbasaur"]["Moves"].update({level[0]: [level[1]]})
moves["Bulbasaur"]["Moves"] = dict(sorted(moves["Bulbasaur"]["Moves"].items()))

print(moves)
#moves["Bulbasaur"]["Moves"][3].append("GROWTH")

#print(moves)
