n, p = map(int, input().split())

notes = [int(input()) for i in range(n)]
notes.sort()

i = 1
lastUsed = notes[0]
count = 1
while i < len(notes):
    if notes[i] > lastUsed+p:
        count += 1
        lastUsed = notes[i]
    i += 1

print(count)