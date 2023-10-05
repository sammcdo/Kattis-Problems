thing = input()

a = 0
b = 0

while len(thing) > 0:
    t = thing[0]
    thing = thing[1::]
    n = []
    if 'A' in thing:
        n.append(thing.index('A'))
    if 'B' in thing:
        n.append(thing.index('B'))
    n.append(len(thing))
    n = min(n)
    p = thing[0:n]
    thing = thing[n::]

    if t == 'A':
        a += int(p)
    else:
        b += int(p)

    if a >= 11 and a-b >= 2:
        print("A")
        break

    if b >= 11 and b - a >= 2:
        print("B")
        break