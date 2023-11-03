n = int(input())

def fme(b, exp, m):
    res = 1
    while exp > 1:
        if exp & 1: # Check if it is odd
            res = (res*b) % m
        b = b**2 % m
        exp >>= 1       # Shift the exponent over 1 in binary
    return (b * res) % m

# print(fme(9,0,1000000007))
for i in range(n):
    x = int(input())

    if x-1 >= 1:
        count = 8 * fme(9, x-1, 1000000007)
    else:
        count = 8

    print(count % 1000000007)