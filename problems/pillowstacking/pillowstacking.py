from math import ceil, log2

n, c = map(int, input().split())
pillows = []

lowest = float('inf')

for i in input().split():
    i = int(i)
    pillows.append(i)
    if i < lowest:
        lowest = i

dp = set([0])

# test all possible stacks that use i pillows
for i in range(int(log2(lowest))):
    nxt = set()
    for x in dp:
        for j in range(len(pillows)):
            thing = x + ceil(pillows[j] / (2**i))
            # don't include results over the target
            if thing <= c:
                nxt.add(thing)
    
    if c in nxt:
        print("YES")
        exit(0)
    dp = nxt
    if len(dp) == 0:
        print("NO")
        exit(0)

# every pillow can be turned into an infinite 
# sequence of pillows of 1 softness after
# log_2(original softness) pillows are stacked
# if there are still results less than the target 
# softness after a 1 sequence is reached you can 
# always get to the solution
if len(dp):
    print("YES")