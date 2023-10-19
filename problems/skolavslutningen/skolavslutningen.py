rows, cols, classes = map(int, input().split())

data = []
for i in range(rows):
    data.append(list(input()))

uniqueCols = []

for col in range(cols):
    this = set()
    for row in range(rows):
        this.add(data[row][col])

    found = False
    for i in range(len(uniqueCols)):
        thing = uniqueCols[i]
        if len(this.intersection(thing)) > 0:
            uniqueCols[i] = thing.union(this)
            found = True
    if not found:
        uniqueCols.append(this)


print(len(uniqueCols))