from sys import stdin

while True:
    try:
        cap, cases = [int(i) for i in stdin.readline().split()]

        weights = []
        values = []
        for i in range(cases):
            a,b = [int(i) for i in stdin.readline().split()]
            values.append(a)
            weights.append(b)

        dp = [[0 for j in range(cap+1)] for i in range(cases+1)]

        for i in range(1, cases+1):
            for j in range(1,cap+1):
                if weights[i-1] <= j:
                    added = values[i-1] + dp[i-1][j-weights[i-1]]
                    not_added = dp[i-1][j]
                    if added >= not_added:
                        dp[i][j] = added
                    else:
                        dp[i][j] = not_added
                else:
                    dp[i][j] = dp[i-1][j]

        inds = []
        for i in range(cases, 0, -1):
            if dp[i][cap] != dp[i-1][cap]:
                inds.append(i-1)
                cap -= weights[i-1]

        print(len(inds))
        for x in inds:
            print(x, end=" ")
        print()

    except Exception as e:
        # print(e)
        break