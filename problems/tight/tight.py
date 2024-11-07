import sys

for line in sys.stdin:
    k, n = map(int, line.split())

    total = (k+1)**n
    valid = 0
    digitCounts = [1 for i in range(0,k+1)]

    for i in range(n-1):
        starts = digitCounts.copy()
        # print(starts)
        digitCounts = [0]*(k+1)
        for j in range(len(starts)):
            for x in range(-1,2):
                if j+x >= 0 and j+x <= k:
                    digitCounts[j+x] += starts[j]
        
    valid = sum(digitCounts)
    
    print(valid/total*100)