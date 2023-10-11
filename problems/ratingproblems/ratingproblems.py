judges, done = map(int, input().split())

sofar = [int(input()) for i in range(done)]

worst = sofar + [-3 for i in range(judges-done)]
best = sofar + [3 for i in range(judges-done)]

print(sum(worst)/judges, sum(best)/judges)