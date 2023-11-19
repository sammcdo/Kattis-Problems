n, a, b, c = map(int, input().split())

cookies = [a, b, c]
cookies.sort(reverse=True)

if cookies[0] > cookies[1] + cookies[2] + n:
    print(2 * (cookies[1] + cookies[2]) + n)
else:
    print(sum(cookies))