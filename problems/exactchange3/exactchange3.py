a = input().rjust(1_000_000, '0')
b = input().rjust(1_000_000, '0')

c = 0
for i in range(len(a)):
    if b[i] == '1' and a[i] == '0':
        c += 1_000_000 - i
        break
    elif b[i] == '1' and a[i] == '1':
        c += 1

# print(a)
# print(b)
print(c)