import collections

n, m = map(int, input().split())

tree = [["-"]*(m+2)] + [list("-" + input() + "-") for i in range(n)] + [["-"]*(m+2)]

# print(tree)

dp = [[float('inf') for i in range(m+2)] for j in range(n+2)]
# print(dp)

queue = collections.deque((i,j) for i in range(n+2) for j in range(m+2) if tree[i][j] == "-")

for i, j in queue:
    dp[i][j] = 0

m += 2
n += 2

highest = 0
while queue:
    node = queue.popleft()
    r = float('inf')
    i, j = node

    if i-1 != -1 and dp[i-1][j] == float('inf'):
        dp[i-1][j] = dp[i][j]+1
        queue.append((i - 1, j))

    if j-1 != -1 and dp[i][j-1] == float('inf'):
        dp[i][j-1] = dp[i][j]+1
        queue.append((i, j-1))

    if i+1 != n and dp[i+1][j] == float('inf'):
        dp[i+1][j] = dp[i][j]+1
        queue.append((i + 1, j))

    if j+1 != m and dp[i][j+1] == float('inf'):
        dp[i][j+1] = dp[i][j]+1
        queue.append((i, j+1))

    dp[i][j] = min(dp[i][j], r)
    if dp[i][j] > highest:
        highest = dp[i][j]

print(highest)