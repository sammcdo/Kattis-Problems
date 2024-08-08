n, m, q = map(int, input().split())

all = set([i+1 for i in range(n)])
data = {}
for i in range(m):
    data[i+1] = set()

for i in range(n):
    line = input()

    for j in range(m):
        if line[j] == "Y":
            data[j+1].add(i+1)

opts = []


target = set()
for i in range(q):
    question = input().split()
    val = int(question[0])

    if i == 0:
        if question[1] == "N":
            target = all-data[val]
        else:
            target = data[val]
        continue

    if question[1] == "N":
        target = target.intersection(all-data[val])
    else:
        target = target.intersection(data[val])

if len(target) == 1:
    print("unique")
    print(list(target)[0])
else:
    print("ambiguous")
    print(len(target))


