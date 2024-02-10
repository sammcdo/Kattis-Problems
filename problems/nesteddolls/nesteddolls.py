from collections import deque
import bisect

numCases = int(input())

def canFit(one, two):
    a1, b1 = one
    a2, b2 = two
    if a1 > a2 and b1 > b2:
        return True
    return False


def search(nums, target):
    i = 0
    j = len(nums) - 1
    loc = len(nums)
    while i <= j:
        k = (i + j) // 2
        if target[1] >= nums[k][1]:
            i = k + 1  # move upper pointer down
        else:
            j = k - 1  # move lower pointer up
            loc = k
    return loc  # not found, return -1

for i in range(numCases):
    input()
    line = [int(i) for i in input().split()]

    stack = deque()
    for i in range(0, len(line), 2):
        stack.append((line[i], -line[i+1]))

    stack = sorted(stack, reverse=True)
    # print(stack)

    done = False
    count = 1
    prev = (float('inf'), float('inf'))
    nests = [prev]

    for doll in stack:
        found = False
        doll = (doll[0], -doll[1])
        if doll[0] == nests[-1][0]:
            nests.append(doll)
        else:
            x = search(nests, doll)
            # print("bisect", x)
            if x < len(nests): # and canFit(nests[x], doll):
                # print("replaced")
                nests[x] = doll
            else:
                # print("added")
                nests.append(doll)

    print(len(nests))
