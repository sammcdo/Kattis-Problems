d = int(input())

rt = int(input())
tt = int(input())

for rage in range(4, 1000):
    tage = rage - d
    if tage < 0:
        continue
    
    rn = rage*(rage+1) / 2 - 6
    tn = tage*(tage+1) / 2 - 3

    if rn + tn == rt+tt:
        print(int(rt-rn))