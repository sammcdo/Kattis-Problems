n, m = [int(i) for i in input().split()]

adj = [[] for i in range(n+1)]
sticks = [0 for i in range(n+1)]

# get all sticks layers
for i in range(m):
    a, b = [int(i) for i in input().split()]
    sticks[b] += 1
    adj[a].append(b)

q = []

# put sticks with nothing on top of them first to be picked up
for i in range(1,n+1):
    if sticks[i] == 0:
        q.append(i)

processed = []
while len(q) > 0:
    curr = q.pop()
    processed.append(curr)
    
    # for each stick drawn check if that uncovers another stick
    for x in adj[curr]:
        sticks[x] -= 1
        if sticks[x] == 0:
            q.append(x)

if len(processed) == n:
    for x in processed:
        print(x)
else:
    print("IMPOSSIBLE")