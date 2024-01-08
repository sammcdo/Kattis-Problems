people = int(input())

names = [input() for i in range(people)]

knocks = int(input())

queries = [input() for i in range(knocks)]

lookup = {}
for i in names:
    temp = i.split()

    if len(temp) == 1:
        lookup[temp[0]] = "Jebb"
    else:
        lookup[temp[0]] = "Neibb en " + temp[0] + " " + temp[1] + " er heima"

for i in queries:
    if i in lookup:
        print(lookup[i])
    else:
        print("Neibb")


