n = int(input())

dist = float('inf')
for i in range(n):
    x_1,y_1,x_2,y_2 = map(int,input().split())

    if x_1 > x_2:
        x_1,y_1,x_2,y_2 = x_2,y_2,x_1,y_1
    
    # print(x_1,y_1,x_2,y_2)
    
    if x_1 <= 0 and x_2 >= 0:
        m = (y_2-y_1)/(x_2-x_1)
        b = y_1 - m*x_1
        if b > 0:
            # print(b)
            dist = min(b, dist)

if dist == float('inf'):
    print(-1)
else:
    print(dist)