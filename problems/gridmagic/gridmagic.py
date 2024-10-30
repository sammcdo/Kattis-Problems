def isPrime(n):
    if n < 2: return False
    if n <= 3: return True
    if not n%2 or not n%3: return False
    for i in range(5, int(n**0.5+1),6):
        if not n%i or not n%(i+2):
            return False
    return True

def search(map, n, m, r, c):
    if r > n:
        # print(map)
        return 1
    if c > m:
        return search(map, n, m, r+1, 0)

    cnt = 0
    cPref = "".join([str(map[i][c]) for i in range(r)])
    rPref = "".join([str(map[r][i]) for i in range(c)])
    for i in range(0,10):
        row = int(rPref + str(i))
        col = int(cPref + str(i))
        if isPrime(row) and isPrime(col):
            map[r][c] = i
            cnt += search(map, n, m, r, c+1)
    return cnt

n, m = map(int, input().split())

map = [[0 for i in range(m)] for _ in range(n)]
cnt = search(map, n-1, m-1, 0, 0)
print(cnt)