n = int(input())

prices = [int(i) for i in input().split()]

prices.sort()

savings = 0

while len(prices) >= 3:
    a = prices.pop()
    b = prices.pop()
    c = prices.pop()

    savings += c

print(savings)