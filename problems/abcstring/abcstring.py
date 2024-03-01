from collections import deque

x = input()
c = deque()

states = {"":0,
          "A":0,
          "B":0,
          "C":0,
          "AB":0,
          "AC":0,
          "BC":0,
}

for k in x:
    c.append(k)

m = 0
h = 0
while c:
    l = c.popleft()
    #print(l, states)

    if l == "A":
        if states["BC"] >= 1:
            states["BC"] -= 1
            states[""] += 1
        elif states["B"] >= 1:
            states["B"] -= 1
            states["AB"] += 1
        elif states["C"] >= 1:
            states["C"] -= 1
            states["AC"] += 1
        elif states[""] >= 1:
            states[""] -= 1
            states["A"] += 1
        else:
            states["A"] += 1
            m += 1
    elif l == "B":
        if states["AC"] >= 1:
            states["AC"] -= 1
            states[""] += 1
        elif states["A"] >= 1:
            states["A"] -= 1
            states["AB"] += 1
        elif states["C"] >= 1:
            states["C"] -= 1
            states["BC"] += 1
        elif states[""] >= 1:
            states[""] -= 1
            states["B"] += 1
        else:
            states["B"] += 1
            m += 1
    elif l == "C":
        if states["AB"] >= 1:
            states["AB"] -= 1
            states[""] += 1
        elif states["B"] >= 1:
            states["B"] -= 1
            states["BC"] += 1
        elif states["A"] >= 1:
            states["A"] -= 1
            states["AC"] += 1
        elif states[""] >= 1:
            states[""] -= 1
            states["C"] += 1
        else:
            states["C"] += 1
            m += 1
    if m > h:
        h = m

print(h)