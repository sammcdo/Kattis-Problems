width = int(input())

area = 0
for i in range(int(input())):
    l, w = map(int, input().split())

    area += l*w

print("%d" % (area / width))