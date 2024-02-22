n = int(input())

fee = float(input())

days = [float(input()) for i in range(n)]

cash = [0 for i in range(len(days))]
stock = [0 for i in range(len(days))]

cash[0] = 100
stock[0] = (100-fee) / days[0]

for i in range(1, len(days)):
    cash[i] = max(cash[i-1], (stock[i-1] * days[i]) - fee)
    stock[i] = max(stock[i-1], (cash[i-1] - fee) / days[i])

print(cash[-1])


