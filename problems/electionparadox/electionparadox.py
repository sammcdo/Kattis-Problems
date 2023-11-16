input()

a = [int(i) for i in input().split()]

a.sort()

s = 0
for i in range(len(a)//2+1):
    s += a[i] // 2

for i in range(len(a)//2+1, len(a)):
    s += a[i]

print(s)

