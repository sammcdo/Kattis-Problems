def seive(lim):
    isPrime = [1]*lim
    isPrime[0] = 0
    isPrime[1] = 0

    for i in range(4, lim, 2):
        isPrime[i] = False
    for i in range(3, int(lim**0.5+1), 2):
        if isPrime[i]:
            j = i*i
            while j < lim:
                isPrime[j] = 0
                j += i*2
    return isPrime

def check(n):
    visited = set()
    while True:
        # print(n)
        if n <= 3:
            break
        nextN = 0
        for i in str(n):
            nextN += int(i)*int(i)
        if nextN in visited:
            return False
        n = nextN
        visited.add(n)
    if n == 1:
        return True
    return False


isPrime = seive(50_000)

for i in range(int(input())):
    x, n = map(int, input().split())
    
    if isPrime[n]:
        if check(n):
            print(x, n, "YES")
        else:
            print(x, n, "NO")
    else:
        print(x, n, "NO")