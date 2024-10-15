x = input()

a = 0
b = 0

for i in range(0, len(x), 2):
    t = x[i]
    p = int(x[i+1])
    if t == "A":
        a += p
    else:
        b += p
    # print(a,b)
    if a >= 11 and a-b >= 2:
        print("A")
        break
    if b >= 11 and b-a >= 2:
        print("B")