monthly = int(input())

r = int(input())
x = 0
for i in range(r):
    x += monthly - int(input())

print(x + monthly)