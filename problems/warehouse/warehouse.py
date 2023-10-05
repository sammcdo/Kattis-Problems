
def doShipment(l):
    d = {}
    for i in range(l):
        line = input().split()
        if line[0] in d:
            d[line[0]] = int(d[line[0]]) + int(line[1])
        else:
            d[line[0]] = int(line[1])


    return d

for i in range(int(input())):
    l = int(input())

    d = doShipment(l)
    print(len(d))
    for l in sorted(sorted(d.items()), key = lambda x:-x[1]):
        print(l[0], l[1])
