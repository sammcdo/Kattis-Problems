a,b,c = map(int, input().split())

ops = [
    lambda x,y: x+y,
    lambda x,y: x-y,
    lambda x,y: x*y,
    lambda x,y: x/y if x%y==0 else 1000**3,
]

smallest = float('inf')
for first in ops:
    x = first(a,b)
    for second in ops:
        y = second(x,c)
        if int(y) == y and y >= 0:
            smallest = min(smallest, y)
print(int(smallest))