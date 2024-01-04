

n = int(input())


arr = [0] * 86400
for i in range(n):
  line = list( map(int, input().split()))

  inters = line[1:]
  for i in range(0, len(inters), 2):
    a = inters[i]
    b = inters[i+1]
    for g in range(a, b+1):
      arr[g] += 1

m = max(arr)
c = arr.count(m)
print(m)
print(c)