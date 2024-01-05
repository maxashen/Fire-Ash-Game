methods = []

with open("pokemonforms.txt", "r") as f1:
    for line in f1:
        if "Evolutions = " in line[:13]:
            newline = line[13:].removesuffix("\n").split(",")
            for i,x in enumerate(newline):
                if i % 3 == 1:
                    method = x
                    if method not in methods:
                        methods.append(method)

meth = "\n".join(methods)

with open("methods_forms.txt", "w") as f2:
    f2.write(meth)
