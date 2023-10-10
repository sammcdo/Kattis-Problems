a, b, c, d = map(int, input().split())

def gcd(x, y):
    while y: x,y = y, x%y
    return x

def lcm(x, y):
    return (x*y)//gcd(x,y)

e = lcm(c,d)
# print(e)
if e == 1:
    print(b-a+1)
else:
    if a % e == 0:
        a -= 1
    if b % e == 0:
        b += 1
    print((b//e)-(a//e))