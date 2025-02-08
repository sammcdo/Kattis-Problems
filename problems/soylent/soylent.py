for i in range(int(input())):
    cals = int(input())
    
    if cals % 400 == 0:
        print(cals // 400)
    else:
        print(cals // 400 + 1)