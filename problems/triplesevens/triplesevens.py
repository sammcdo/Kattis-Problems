n = int(input())

found = True
for i in range(3):
    if "7" not in input():
        found = False
        break

if found == False:
    print(0)
else:
    print(777)