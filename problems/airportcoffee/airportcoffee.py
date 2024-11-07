import bisect

l, a, b, t, r = map(float, input().split())
n = int(input())
carts = list(map(float, input().split())) + [l]

best = [(0, 0)]*(n+1)

for i in range(n-1, -1, -1):
    best[i] = (best[i+1][0] + (carts[i+1]-carts[i]) / a, i+1)
    j = bisect.bisect(carts, carts[i] + a*t + b*r)
    if j <= n:
        best[i] = min(best[i], (best[j][0] + t + r + (carts[j]-carts[i]-a*t-b*r)/a, j))
    if j-1 > i and carts[j-1] - carts[i] > a*t:
        best[i] = min(best[i], (best[j-1][0] + t + (carts[j-1]-carts[i]-a*t)/b, j-1))

sol = []
at = 0
while at < n:
    sol.append(at)
    at = best[at][1]

print (len(sol))
print (' '.join(map(str, sol)))