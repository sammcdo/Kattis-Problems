from fractions import Fraction as F
n, a, b, days = map(int, input().split())

states = {(a,b): F(1)}

moves = [(-1,-1), (1,-1), (1,1), (-1,1)]

def bound(x):
    return max(min(x, n),1)

works = F(0,1)
for _ in range(days):
    new_states = {}
    # print(states)

    for x in range(1,n+1):
        for y in range(1,n+1):
            if (x,y) in states:
                for m in moves:
                    nx = bound(x+m[0])
                    ny = bound(y+m[1])
                    if nx == ny:
                        works += states[(x,y)] / 4
                    else:
                        if (nx,ny) not in new_states:
                            new_states[(nx,ny)] = F(0,1)
                        new_states[(nx,ny)] += states[(x,y)] / 4
    states = new_states
    # print(states)
    # print()

# print(works)
if works == 0:
    print("0/1")
else:
    print(works)

