points = [input().split() for i in range(3)]

xs = [int(i[0]) for i in points]
ys = [int(i[1]) for i in points]

point = [0,0]
for i in xs:
    if xs.count(i) == 1:
        point[0] = i

for i in ys:
    if ys.count(i) == 1:
        point[1] = i

print(point[0], point[1])