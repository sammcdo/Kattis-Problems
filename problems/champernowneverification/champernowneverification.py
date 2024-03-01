s = input()

n = 1
ptr = 0
while ptr < len(s):
    if s[ptr:ptr+len(str(n))] != str(n):
        print(-1)
        quit()

    ptr += len(str(n))
    n += 1

print(n-1)