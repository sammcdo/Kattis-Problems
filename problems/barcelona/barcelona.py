n, x = map(int, input().split())
bags = [int(i) for i in input().split()]
loc = bags.index(x)
if loc == 0:
    print("fyrst")
elif loc == 1:
    print("naestfyrst")
else:
    print(loc+1, "fyrst")