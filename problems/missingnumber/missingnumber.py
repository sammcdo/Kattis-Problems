n = int(input())
data = list(input())

p = 0
found = False
for i in range(1,n+1):
    s = str(i)
    for j in range(len(s)):
        if not data[p+j] == s[j]:
            print(s)
            found=True
            break
    if found:
        break
    p += len(s)
    if p >= len(data):
        print(i+1)
        break