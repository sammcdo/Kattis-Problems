import sys

n = int(sys.stdin.readline())

skillA = []
skillB = []
skillC = []
used = set()
for i in range(n):
    name, a, b, c = sys.stdin.readline().split()
    a,b,c = map(int, [a,b,c])
    
    skillA.append((-a, name))
    skillB.append((-b, name))
    skillC.append((-c, name))

skillA.sort()
skillB.sort()
skillC.sort()
a = 0
b = 0
c = 0

# print(skillA)
teams = []
while True:
    teams.append([])
    while a < len(skillA):
        nextA = skillA[a]
        if nextA[1] not in used:
            teams[-1].append(nextA[1])
            used.add(nextA[1])
            break
        a+=1
    while b < len(skillB):
        nextB = skillB[b]
        if nextB[1] not in used:
            teams[-1].append(nextB[1])
            used.add(nextB[1])
            break
        b+=1
    while c < len(skillC):
        nextC = skillC[c]
        if nextC[1] not in used:
            teams[-1].append(nextC[1])
            used.add(nextC[1])
            break
        c+=1
    if len(teams[-1]) != 3:
        teams.pop(-1)
        break

for t in teams:
    t = sorted(t)
    for p in t:
        print(p, end=" ")
    print()