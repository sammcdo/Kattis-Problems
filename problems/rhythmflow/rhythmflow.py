n, m = map(int, input().split())

actual = [int(input()) for i in range(n)]
guess = [int(input()) for i in range(m)]

dp = [[0 for _ in range(m+1)] for i in range(n+1)]

lookup = {
    (0,15):7,
    (16,23):6,
    (24,43):4,
    (44,102):2
}
# print(actual, guess)

start = 0
for i in range(1, n+1): # loop through actual
    # print("start", start, end=" ")
    # g = guess[start]
    # a = actual[i-1]
    # while abs(g-a) > 102 and start < len(guess)-1 and abs(g-actual[i]) > 102:
    #     start+=1
    #     if start < len(guess):
    #         g = guess[start]
    #     else:
    #         g -= 1
    # print(start)
    for j in range(1, m+1): # loop through guesses
        anyUsed = False
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        g = guess[j-1]
        a = actual[i-1]
        # print(a,g)
        found = False
        for x, v in lookup.items():
            if abs(g-a) >= x[0] and abs(g-a) <= x[1]:
                dp[i][j] = max(dp[i-1][j-1] + v, dp[i][j])
                found = True
                anyUsed = True
        if not found and anyUsed:
            break

# for i in dp:
    # print(i)

print(dp[-1][-1])
