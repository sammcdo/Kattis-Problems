for _ in range(int(input())):
    x,y = map(float, input().split())

    found = False
    for i in range(int(input())):
        a,b = map(float, input().split())
        if (abs(x-a)**2 + abs(y-b)**2)**0.5 <= 8 and not found:
            print("light a candle")
            found = True
    if not found:
        print("curse the darkness")