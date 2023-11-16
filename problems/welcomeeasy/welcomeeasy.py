cases = int(input())

test = "welcome to code jam"

for x in range(cases):
    comp = input()

    dp = [0] * (len(test)+1)
    dp[0] = 1
    for i in range(len(comp)):
        for j in range(len(test)):
            if comp[i] == test[j]:
                dp[j+1] += dp[j]
                dp[j+1] = dp[j+1] % 10000

    print("Case #"+str(x+1)+": "+str(dp[-1]).rjust(4, "0"))
