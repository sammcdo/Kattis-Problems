a = []
for i in range(5):
    a.append(sum(map(int, input().split())))
i = a.index(max(a))+1
print(i, max(a))