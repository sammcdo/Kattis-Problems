import sys
from bisect import bisect_left, bisect_right

n, q = [int(i) for i in sys.stdin.readline().split()]

store = {}

for i in sys.stdin.readline().split():
    i = int(i)
    if i in store:
        store[i] += 1
    else:
        store[i] = 1

probs = sorted(list(store.keys()))

for i in range(q):
    kind, num = [int(i) for i in sys.stdin.readline().split()]

    if kind == 1:
        x = bisect_right(probs, num)
        found = False
        while x < len(probs):
            y = probs[x]
            if y > num and store[probs[x]] > 0:
                found = True
                print(probs[x])
                store[probs[x]] -= 1
                break
            x += 1
        if not found:
            x = -1
            print(-1)
    else:
        x = bisect_left(probs, num)
        found = False
        if x == len(probs):
            x -= 1
        while x >= 0:
            y = probs[x]
            if y <= num and store[probs[x]] > 0:
                found = True
                print(probs[x])
                store[probs[x]] -= 1
                break
            x -= 1
        if not found:
            x = -1
            print(-1)
