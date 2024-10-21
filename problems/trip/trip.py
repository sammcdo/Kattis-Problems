while True:
    n = int(input())
    if n == 0:
        break

    dollars = [int(float(input())*100+0.5) for _ in range(n)]
    dollars.sort()
    s = sum(dollars)
    avg = s // n
    extraPennies = int(s - (avg * n))

    transferred = 0
    # people with extra penny
    for i in range(n-1, n-extraPennies-1, -1):
        if dollars[i] > avg+1:
            transferred += dollars[i]-(avg+1)
    # people not with extra penny
    for i in range(n-extraPennies-1, -1, -1):
        if dollars[i] > avg:
            transferred += dollars[i]-avg
    print("$%d.%02d" % (transferred//100, transferred % 100))
    # print()