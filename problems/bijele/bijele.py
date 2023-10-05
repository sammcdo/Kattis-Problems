l = [1,1,2,2,2,8]

a = [int(i) for i in input().split()]
b = []

for i in range(len(a)):
    b.append(str(l[i] - a[i]))

print(" ".join(b))