n = int(input())
high = float('inf')
low = -1
for i in range(n):
    a,b = map(int, input().split())
    low = max(low,a)
    high = min(high,b)

if high < low:
    print('bad news')
else:
    print(high-low+1, low)