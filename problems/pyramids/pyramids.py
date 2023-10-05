num = int(input())

size = 1
c = 0

if num == 1:
    print(1)
else:
    while num >= 0:
        num -= size**2
        size += 2
        c+= 1
    
    print(c-1)