n, m, k = map(int, input().split())

days = [int(input()) for _ in range(n)]
days = days + [0 for _ in range(m)]
# print(days)

paid = [0 for _ in range(len(days))]

curr = 0
flights = 0
highest = 0
for i in range(len(days)):
    flights += days[i]
    if i-m >= 0:
        flights -= days[i-m]
        curr -= paid[i-m]

    x = i
    while flights - curr > 0 and k - curr > 0 and x >= 0 and x > i-m:
        canPay = min(days[x]-paid[x], k-curr)
        paid[x] += canPay
        curr += canPay
        highest += canPay
        x -= 1


# print(days)
# print(paid)
print(highest)
