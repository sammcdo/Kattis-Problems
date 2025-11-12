n,m = map(int, input().split())

allLists = set(input().split())

for _ in range(n-1):
    allLists = allLists.intersection(set(input().split()))

print(len(allLists))
for i in sorted(allLists):
    print(i)