pres = {}

for i in range(int(input())):
    p = input()
    x = input()
    pres[p] = [x,0]

for i in range(int(input())):
    x = input()
    if x in pres:
        pres[x][1] += 1

best = list(i[1] for i in pres.values())
best.sort()
if best[-1] == best[-2]:
    print("tie")
    exit(0)

# print(best)
for k,v in pres.items():
    if v[1] == best[-1]:
        print(v[0])
        exit(0)
