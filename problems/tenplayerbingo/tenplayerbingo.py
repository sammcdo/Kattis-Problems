order = [i for i in input().split()]

lookup = {i:0 for i in "1234567890"}

done = []
for n in order:
    b = n[-1]
    
    lookup[b] += 1
    
    if lookup[b] == 10:
        done.append(b)

if order[-1][-1] == "0":
    print(10)
else:
    print(order[-1][-1])