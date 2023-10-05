n = int(input())
prices = [int(i) for i in input().split()]

s = sum(prices)
offset = 0

counts = {}
for i in prices:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == "INFLATION":
        inf = int(cmd[1])
        s += n * inf
        offset += inf
        print(s)
    else:
        a = int(cmd[1])
        b = int(cmd[2])
        if a - offset in counts:
            x = counts[a-offset]
            del counts[a-offset]
            if b-offset in counts:
                counts[b-offset] += x
            else:
                counts[b-offset] = x
            s += x * (b-a)
        print(s)
