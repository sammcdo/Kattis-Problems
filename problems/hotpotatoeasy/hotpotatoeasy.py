p, t = map(int, input().split())
players = []
toys = []
for i in range(p):
    players.append(input())
for i in range(t):
    toys.append(int(input()))

p_i = 0
t_i = 0

while len(players) > 1:
    p_i = (p_i + toys[t_i]) % len(players)
    t_i = (t_i + 1) % t
    players.remove(players[p_i])
print(*players)