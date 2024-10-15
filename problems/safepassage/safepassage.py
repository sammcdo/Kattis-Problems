n = [int(i) for i in input().split()]

here = n[1:]
here.sort()

n = len(here)

moves = [0, here[1]]

for i in range(2,n):
    # run run fastest back, run ith over
    optA = moves[i-1] + here[0] + here[i]
    # undo prev move
    # run second fastest back, run ith and i-1th over, run fastest back, run second fastest over
    # basically two moves here
    optB = moves[i-2] + here[i] + here[1] + here[1] + here[0]
    moves.append(min(optA, optB))
    # print(moves)

# print(moves, n)
print(moves[n-1])

