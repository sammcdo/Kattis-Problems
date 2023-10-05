a = input()
p = a[0]
for i in range(1, len(a)):
    if a[i] == p[-1]:
        pass
    else:
        p += a[i]
print(p)