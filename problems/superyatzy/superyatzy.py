dice, flips = map(int, input().split())

l = {}

for i in range(dice):
    x = input()
    if x not in l:
        l[x] = 0
    l[x] += 1
    

for k,v in l.items():
    if v+flips >= dice:
        print("Ja")
        exit(0)
print("Nej")