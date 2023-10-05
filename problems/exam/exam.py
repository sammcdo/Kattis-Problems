k=int(input())
yours = list(input())
theirs = list(input())

score = 0
opp = 0
for i in range(len(yours)):
    if yours[i] == theirs[i]:
        if k > 0:
            score += 1
            k -= 1

    else:
        opp += 1

score += max(0, opp-k)

print(score)