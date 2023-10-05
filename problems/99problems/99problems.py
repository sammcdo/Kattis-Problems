numS = input()
num = int(numS)

if num < 99:
    print(99)
else:
    if len(numS) < 4:
        placeValue = len(numS) - 1

        up = int(numS[0]) * (10**placeValue) + 99
        down = int(numS[0]) * (10**placeValue) - 1

    else:
        div = len(numS[:-2]) % 2
        placeValue = len(numS) - 2 - div

        up = int(numS[:-2]) * (10 ** placeValue) + 99
        down = int(numS[:-2]) * (10 ** placeValue) - 1
    if up - num == num - down:
        print(up)
    elif num - down < up - num:
        print(down)
    else:
        print(up)
