x = input()

states = {
    "":1,
    "A":0,
    "B":0,
    "C":0,
    "AB":0,
    "AC":0,
    "BC":0,
}

for letter in x:
    if letter == "A":
        if states["BC"] >= 1:
            states["BC"] -= 1
            states[""] += 1
        elif states["B"] >= 1:
            states["B"] -= 1
            states["AB"] += 1
        elif states["C"] >= 1:
            states["C"] -= 1
            states["AC"] += 1
        elif states[""] >= 1:
            states[""] -= 1
            states["A"] += 1
        else:
            states["A"] += 1
    if letter == "B":
        if states["AC"] >= 1:
            states["AC"] -= 1
            states[""] += 1
        elif states["A"] >= 1:
            states["A"] -= 1
            states["AB"] += 1
        elif states["C"] >= 1:
            states["C"] -= 1
            states["BC"] += 1
        elif states[""] >= 1:
            states[""] -= 1
            states["B"] += 1
        else:
            states["B"] += 1
    if letter == "C":
        if states["AB"] >= 1:
            states["AB"] -= 1
            states[""] += 1
        elif states["B"] >= 1:
            states["B"] -= 1
            states["BC"] += 1
        elif states["A"] >= 1:
            states["A"] -= 1
            states["AC"] += 1
        elif states[""] >= 1:
            states[""] -= 1
            states["C"] += 1
        else:
            states["C"] += 1

print(sum(states.values()))





