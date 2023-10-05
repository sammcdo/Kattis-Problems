a,b = map(int, input().split())
s = 0
for i in range(a):
    s += int(input())

if s <= b:
    print("Jebb")
else:
    print("Neibb")