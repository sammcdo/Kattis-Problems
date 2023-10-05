n = int(input())

for i in range(n):
    c, days = map(int, input().split())
    s = sum([i for i in range(1,days+1)])
    s+= days
    print(c, s)