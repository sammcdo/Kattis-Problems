def convert(this):
    if this >= '0' and this <= '9':
        return int(this)
    elif this >= 'a' and this <= 'z':
        return (ord(this) - ord('a') + 10)
    else:
        return (ord(this) - ord('A') + 36)

for _ in range(int(input())):
    a = input()
    b = input()

    if a > b:
        a, b = b, a

    if len(a) > len(b):
        print("NO")
        continue
    if len(a) < len(b):
        print("YES")
        continue

    i = 0
    while a[i] == b[i]:
        i += 1
        continue

    if convert(a[i]) < convert(b[i]):
        print("YES")
    else:
        print("NO")
    