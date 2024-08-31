n, m = map(int, input().split())

notes = {}

for i in range(n):
    this = [int(i) for i in input().split()][1::]
    for a in this:
        if a in notes:
            notes[a].add(i)
        else:
            notes[a] = set()
            notes[a].add(i)

song = [int(i) for i in input().split()]
instruments = set()
changes = 0
for note in song:
    instruments = instruments.intersection(notes[note])
    if len(instruments) == 0:
        changes += 1
        instruments = notes[note]

print(changes-1)