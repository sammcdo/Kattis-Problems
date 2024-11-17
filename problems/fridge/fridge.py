number = input()

counts = {i:0 for i in range(0,10)}

for n in number:
    n = int(n)

    counts[n] += 1

counts[0] += 1

failed = ''
minDigit = 0
minC = counts[0]
for i in range(10):
    if counts[i] < minC:
        minC = counts[i]
        minDigit = i

if minDigit == 0:
    failed += '1'
    minC -= 1

for i in range(minC+1):
    failed += str(minDigit)

print(failed)