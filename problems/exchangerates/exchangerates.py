import math

n = int(input())

while n != 0:

    CAD = 1000
    USD = 0

    for i in range(n):
        rate = float(input())

        newCAD = math.floor(USD * rate * 0.97 * 100) / 100

        if newCAD > CAD:
            CAD = newCAD
            continue

        newUSD = math.floor(CAD / rate * 0.97 * 100) / 100

        if newUSD > USD:
            USD = newUSD

    print("%.2f" % CAD)

    n = int(input())

