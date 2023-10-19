import sys
n = [int(i) for i in input()]

for i in range(len(n)-2, -1, -1):
    if n[i] < n[i+1]:
        m = float("inf")
        ind = i+1
        for j in range(i+2, len(n)):
            if n[j] > n[i] and n[j] < m:
                m = n[j]
                ind = j
        n[ind], n[i] = n[i], n[ind]

        n[i+1::] = sorted(n[i+1::])

        for x in n:
            print(x, end="")
        sys.exit()

print(0)