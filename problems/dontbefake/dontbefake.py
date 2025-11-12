n = int(input())
da = [0 for i in range(86401)]
for i in range(n):
    x = list(map(int, input().split()))
    for i in range(1, x[0]*2+1, 2):
        lower, upper = x[i], x[i+1]
        da[lower] += 1
        da[upper+1] -= 1
# arr = [0 for i in range(86400)]
count = 0
curr = 0
maximum = 0
for i in range(86401):
    # if da[i] > 0:
    count += da[i]
    
    # arr[i] = count
    if count == maximum:
        curr += 1
    elif count > maximum:
        curr = 1
        maximum = count
    
    # if da[i] < 0:
    #     count += da[i]
print(maximum, curr, sep='\n')
# print(da[:100])
# print(arr[:100])