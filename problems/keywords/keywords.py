thing = set()

for i in range(int(input())):
    a = input().lower().replace("-", " ")

    thing.add(a)

print(len(thing))