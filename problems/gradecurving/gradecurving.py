import math
c, ylow, yhigh = map(int, input().split())


min_k = -1
max_k = -1
# def curve(k, inp):
#     if k == 0:
#         return inp
#     else:
#         return curve(k-1, 10*math.sqrt(inp))


i = 0
while True:
    
    if math.ceil(c) >= ylow and min_k == -1:
        min_k = i

    if c > yhigh:
        max_k = i - 1

    i += 1
    if min_k > -1 and max_k > -1:
        break
    if i > 10**6:
        max_k = "inf"
        break
    c = 10*math.sqrt(c)

if max_k != "inf" and min_k > max_k :
    print("impossible")
else:
    print(min_k, max_k)