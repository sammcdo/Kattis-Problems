species = {}

planetTotals = {}

for i in range(int(input())):
    row = input().split()

    for spec in row[2::]:
        species[spec] = row[0]

    planetTotals[row[0]] = 0

for i in range(int(input())):
    row = input().split()

    planetTotals[species[row[1]]] += int(row[0])

keys = sorted(list(planetTotals.keys()))

for i in keys:
    print(i, planetTotals[i])