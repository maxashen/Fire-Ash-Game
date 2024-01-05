headers = []

with open("pokemonforms.txt", "r") as f1:
    for line in f1:
        if " = " in line:
            header = line[:line.find(" ")]
            if header not in headers:
                headers.append(header)

head = "\n".join(headers)

with open("headers_forms.txt", "w") as f2:
    f2.write(head)
