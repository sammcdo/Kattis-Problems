s = 0

for i in range(int(input())):
    f = input()
    n = int(f[0:len(f)-1])
    p = int(f[-1])

    s += n**p

print(s)