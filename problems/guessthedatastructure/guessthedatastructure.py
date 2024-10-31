import sys
from collections import deque
import heapq

for n in sys.stdin:
    stack = []
    queue = deque()
    prque = []
    works = [1,1,1]

    for i in range(int(n)):
        cmd, val = map(int, input().split())

        if cmd == 1:
            stack.append(val)
            queue.append(val)
            heapq.heappush(prque, -val)
        else:
            if len(stack) > 0:
                x = stack.pop(-1)
                if x != val:
                    works[0] = 0
            else:
                works[0] = 0
            if len(queue) > 0:
                x = queue.popleft()
                if x != val:
                    works[1] = 0
            else:
                works[1] = 0
            if len(prque) > 0:
                x = -heapq.heappop(prque)
                if x != val:
                    works[2] = 0
            else:
                works[2] = 0
    
    if sum(works) > 1:
        print("not sure")
    elif sum(works) == 0:
        print("impossible")
    else:
        if works[0]:
            print("stack")
        if works[1]:
            print("queue")
        if works[2]:
            print("priority queue")