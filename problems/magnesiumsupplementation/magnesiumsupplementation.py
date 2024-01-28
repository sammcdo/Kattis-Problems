import math

def getFactors(n):
    f = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            f.add(i)
            f.add(n // i)
    return sorted(list(f))

n, k, p = map(int, input().split())

outputs = []

factors = getFactors(n)

for f in factors:
    b = n // f
    if f <= k and b <= p:
        outputs.append(f)

print(len(outputs))
outputs.sort()
for v in outputs:
    print(v)