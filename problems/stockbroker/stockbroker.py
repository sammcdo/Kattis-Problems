# Stockbroker

days = int(input())

prices = [int(input()) for _ in range(days)]
prices.append(-1)

dp = []

money = 100
bought = 0
lastPrice = 0
for i in range(len(prices)):
    # print(prices[i], money)
    if bought and prices[i] < prices[i-1]:
        money += bought * (prices[i-1] - lastPrice)
        bought = 0
        lastPrice = 0
        # print("\tSell", prices[i] <= money, bought == 0)
    if bought == 0 and prices[i] <= money:
        bought = min(money // prices[i], 100000)
        lastPrice = prices[i]
        # print("\tBought", lastPrice, bought)

print(money)