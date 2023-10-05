for i in range(int(input())):
    a, b = map(float, input().split())
    
    print((a-1)*60/b, (a)*60/b, (a+1)*60/b)