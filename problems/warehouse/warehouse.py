from collections import defaultdict

n = int(input())

for i in range(n):
    m = int(input())
    
    inventory = defaultdict(int)
    
    for i in range(m):
        name, num = input().split()
        num = int(num)
        
        # if name not in inventory:
        #     inventory[name] = 0
        inventory[name] += num
    
    log = []
    for k, v in inventory.items():
        log.append([-v, k])
    
    log.sort(reverse=False)
    
    print(len(log))
    for item in log:
        print(item[1], -item[0])