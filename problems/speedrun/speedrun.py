minT, n = map(int, input().split())

tasks = [[int(i) for i in input().split()] for _ in range(n)]
tasks.sort()

dp = [0 for _ in range(24001)]

for i in range(len(tasks)):
    start = tasks[i][0]
    end = tasks[i][1]

    dp[end] = dp[start] + 1

    # fill forward
    nextPos = len(dp)
    if i < len(tasks)-1:
        nextPos = tasks[i+1][0]+1
    
    for j in range(end, nextPos):
        dp[j] = dp[end]

if minT <= dp[-1]:
    print("YES")
else:
    print("NO")