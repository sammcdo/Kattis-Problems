l, a, b, c, d, e, f = map(int, input().split())

while l:
    x = a / b
    y = c / d
    z = e / f
    n = (1/3 < x < 2/3) \
      + (1/3 < y < 2/3) \
      + (1/3 < z < 2/3)
    
    if n >= 2:
        print(0)
        quit()

    a = (a * 3) % b
    c = (c * 3) % d
    e = (e * 3) % f
    l -= 1

print(1)