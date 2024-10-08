from collections import deque
n, n_songs = map(int, input().split())

members = []

songLookup = []

for i in range(n):
    songs = [int(x) for x in input().split()]
    members.append(songs)

lookup = {}
atN = set()
for i in range(n_songs):
    for j in range(n):
        if members[j][i] not in lookup:
            lookup[members[j][i]] = 0
        lookup[members[j][i]] += 1
        if lookup[members[j][i]] == n:
            del lookup[members[j][i]]
            atN.add(members[j][i])
    if len(lookup) == 0 and len(atN) > 0:
        break

# for k in songLookup:
    # print(k)

print(len(atN))
print(*sorted(atN))