input()

a = list(map(int, input().split()))
b = sorted(a)

count = 0
for i in range(len(a)):
    if a[i] != b[i]:
        count += 1

print(count)