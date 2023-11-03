t = int(input())

l = {}

found = False
for i in range(200001):
    a = i**2
    if a-t in l:
        print(l[a-t], i)
        found = True
        break
    if found:
        break
    l[a] = i

if not found:
    print("impossible")
