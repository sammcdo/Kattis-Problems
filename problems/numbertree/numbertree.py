line = input()
values = line.split()
h=0
seq =""
if len(values) == 1:
    h = int(values[0])
else:
    h_, seq = values
    h = int(h_)

label = 2 ** (h+1) - 1
pos = 0
for (i, s) in enumerate(seq):
    if s == "L":
        pos *= 2
    elif s == "R":
        pos = pos * 2 + 1


label = 2**(h+1)- 2**(len(seq)) - pos
print(label)