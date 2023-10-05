for i in range(int(input())):
    a,b,c = map(int, input().split())
    
    if a < b-c:
        print("advertise")
    elif a > b-c:
        print("do not advertise")
    else:
        print("does not matter")