l, w = map(int, input().split())

m = 10**9 + 7

def tri(a):
    return ((a)*(a-1) // 2) % m

print((tri(l) * tri(w)) % m)