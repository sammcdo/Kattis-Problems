n = int(input())

things = []
for i in range(n):
    name, num = input().split()
    things.append((int(num), name))

things.sort(reverse=True, key=lambda x: x[0])

print(things[0][1])