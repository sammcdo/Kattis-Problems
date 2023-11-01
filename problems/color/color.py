n, c, k = map(int, input().split())

s = list(map(int, input().split()))

s.sort()

count = 0
min_washer = 340234033
capacity = c
for i in range(len(s)):
    v = s[i]
    if capacity == 0:
        count += 1
        capacity = c -1
        min_washer = v
    elif v <= min_washer + k:
        min_washer = min(v, min_washer)
        capacity -= 1
    else:
        count += 1
        capacity = c -1
        min_washer = v

print(count + 1)