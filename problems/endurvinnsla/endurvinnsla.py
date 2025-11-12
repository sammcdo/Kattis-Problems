input()
pct = float(input())
n = int(input())

pcount = 0
for i in range(n):
    thing = input()
    
    if thing != "plast":
        pcount += 1

if pcount / n <= pct:
    print("Jebb")
else:
    print("Neibb")