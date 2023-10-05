var = 7

for i in range(int(input())):
    cmd = input()
    if "op" in cmd:
        var += 1
    else:
        var -= 1
    var = max(var, 0)
    var = min(10, var)

print(var)