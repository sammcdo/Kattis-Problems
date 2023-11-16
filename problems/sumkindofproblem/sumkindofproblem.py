p = int(input())

for i in range(p):
    k, n = map(int, input().split())

    s1 = sum([i for i in range(n+1)])
    s2 = sum([i for i in range(1, 2*n, 2)])
    s3 = sum([i for i in range(2, 2*n+1, 2)])

    print(k, s1, s2, s3)

