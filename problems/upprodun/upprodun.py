g = int(input())
t = int(input())

data = [0 for i in range(g)]

i = 0
while t > 0:
    t -= 1
    data[i] = data[i] + 1
    i += 1
    if i == len(data):
        i = 0

for i in data:
    for d in range(i):
        print("*", end="")
    print()