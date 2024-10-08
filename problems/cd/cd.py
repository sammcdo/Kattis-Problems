while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    x = 0
    jack = set(int(input()) for i in range(n))
    for i in range(m):
        y = int(input())
        if y in jack:
            x += 1
    
    print(x)