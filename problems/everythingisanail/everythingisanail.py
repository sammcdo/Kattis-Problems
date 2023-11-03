import itertools

n = int(input())
building = [int(input()) for i in range(n)][::-1]

states = []
for i in range(4):
    states += itertools.permutations((0,1,2), i)

memo = {s:0 for s in states}
for x in building:
    nxt = {s:0 for s in states}
    for s in states:
        if not s:
            nxt[s] = memo[s]
        elif x == s[-1]:
            nxt[s] = memo[s] + 1
        else:
            nxt[s] = max(nxt[s[:-1]], memo[s])
    memo = nxt

# print(memo)
print(max(memo.values()))