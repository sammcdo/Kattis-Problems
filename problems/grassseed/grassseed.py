cost = float(input())
lawns = int(input())

tot = 0
for i in range(lawns):
    x,y = map(float, input().split())
    
    tot += x*y*cost

print(tot)