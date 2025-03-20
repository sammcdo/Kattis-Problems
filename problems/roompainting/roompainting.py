n, m = map(int, input().split())

buckets = [int(input()) for _ in range(n)]

paints = [int(input()) for _ in range(m)]


def binarySearch(arr, x):
    l = 0
    r = len(arr) - 1
    best = -1
    while l <= r:
        mid = l + (r-l) //2 
        if arr[mid] >= x:
            best = mid
            r = mid -1
        else:
            l = mid + 1
    return arr[best]
    
buckets.sort()
paints.sort()
excessLiters = 0
bi = 0
for paint in paints:
    while buckets[bi] < paint:
        bi += 1
    excessLiters += buckets[bi] - paint

    
print(excessLiters)