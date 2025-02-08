stops, n, start, end = map(int, input().split())

wakes = list(map(int, input().split()))

wakes = [start] + wakes + [end]

up = 1 if wakes[0] <= wakes[1] else 0


changes = 0
for i in range(1, len(wakes)):
    if i == len(wakes) - 1:
        if up and wakes[i-1] < wakes[i]:
            # going correct direction
            continue
        elif not up and wakes[i-1] >= wakes[i]:
            continue
        else:
            changes += 1
            continue
    if up and wakes[i-1] <= wakes[i]:
        # going correct direction
        continue
    elif not up and wakes[i-1] >= wakes[i]:
        # going correct direction
        continue
    elif up and wakes[i-1] > wakes[i]:
        # was up but flipped
        up = False
        changes += 1
    else:
        # was down but flipped
        up = True
        changes += 1

print(changes)