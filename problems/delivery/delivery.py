n, cap = map(int, input().split())

routesUp = []
routesDown = []
for i in range(n):
    route, needed = map(int, input().split())
    if route > 0:
        routesUp.append([route, needed])
    else:
        routesDown.append([-route, needed])

routesUp.sort(reverse=True)
routesDown.sort(reverse=True)

def cost(routes):
    if len(routes) == 0:
        return 0
    total = 0
    has = 0
    i = 0
    while i < len(routes):
        if has >= routes[i][1]:
            has -= routes[i][1]
            i += 1
        else:
            routes[i][1] -= has
            total += routes[i][0] * 2
            has = cap
    # total += routes[-1][0]
    return total
        
t = cost(routesDown) + cost(routesUp)
print(t)