import bisect

n, elo = map(int, input().split())
# all opponents
players = []

for i in range(n):
    l, r, a = map(int, input().split())
    
    players.append((l,r,a))
# sort opponents by easiest (lowest max score)
# ensures we do not have to backtrack to find another possibility
players.sort(key=lambda x: x[1::])
# possible states
canHit = [elo]
# loop through each opponent, assume only fighting that opponent but can start with at any elo in canHit
for opponent in players:
    # find range of elos that can face this opponent
    first = bisect.bisect_left(canHit, opponent[0])
    last = bisect.bisect_right(canHit, opponent[1])

    opts = set(canHit[first:last])
    # fight opponent until number of new elos stops changing
    l = 0
    while len(opts) != l:
        l = len(opts)
        old = opts.copy()
        for i in old:
            if i <= opponent[1]:
                opts.add(i+opponent[2])
    
    # recreate sorted list of elos for next opponent
    canHit = canHit[0:first] + list(opts) + canHit[last::]
    canHit.sort()

print(canHit[-1])