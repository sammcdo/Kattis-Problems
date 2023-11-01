a,b,h = map(int, input().split())

curr = 0
times = 0
while 1:
    curr += a
    times += 1
    if curr >= h:
        print(times)
        quit()
    curr -= b