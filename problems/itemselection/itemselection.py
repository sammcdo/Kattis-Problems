import math

n, m, s, p, q = map(int, input().split())
pp = []
qq = []
for i in range(p):
    pp.append(int(input()))
for i in range(q):
    qq.append(int(input()))
clicks = 0
pages = math.ceil(n / m)

# Bads
bad = [s]  # page nums
i = 1
for beg in range(0, n, m):
    for item in range(beg + 1, min(beg + m, n) + 1):
        if (item in pp) != (item in qq):
            bad.append(i)
            break
    i += 1

# Next/prev page
span = max(bad) - min(bad)
magnet = min(abs(s - max(bad)), abs(s - min(bad)))
clicks += span + magnet

# Section toggle checkboxes
i = 0

for beg in range(0, n, m):
    i += 1
    delta = 0
    qqc = 0
    totalResults = 0
    for result in range(beg + 1, min(beg + m, n) + 1):
        if (result in pp) != (result in qq):
            delta += 1
        if result in qq:
            qqc += 1
        totalResults += 1

    moreClicks = min(delta, 1 + qqc, 1 + totalResults - qqc)

    clicks += moreClicks

# Output
print(clicks)