gold = 29_370
tungsten = 29_260

weight, stacks = map(int, input().split())

s = 0
for i in range(1,stacks+1):
    s += gold*i
    t = s
    for j in range(i+1, stacks+1):
        t += tungsten*j
    if t == weight:
        print(i)
        exit()
    s -= gold*i
    s += tungsten*i
