money = int(input())

fives = money // 500
money = money % 500
if 500 > money and money >= 400:
    fives += 1
    print(fives)
    exit(0)

twos = money // 200
money = money % 200
if 200 > money and money >= 100:
    twos += 1
    print(fives+twos)
    exit(0)

ones = money // 100
money = money % 100

if money > 0:
    ones += 1

print(fives+twos+ones)