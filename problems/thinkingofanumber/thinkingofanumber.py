while True:
    n = int(input())
    if n == 0:
        break

    _min = 0
    _max = float('inf')

    divs = []
    for i in range(n):
        cmd = input()
        if cmd.startswith("less"):
            _max = min(_max, int(cmd.split()[-1]))
        
        elif cmd.startswith("greater"):
            _min = max(_min, int(cmd.split()[-1]))
        
        else:
            divs.append(int(cmd.split()[-1]))
    
    matches = []
    if _max == float('inf'):
        print("infinite")
        continue

    for i in range(_min+1, _max):
        fail = False
        for j in divs:
            if i % j != 0:
                fail = True
                break
        if not fail:
            matches.append(str(i))
        # if len(divs) == 0:
        #     matches.append(str(i))
    
    if len(matches):
        print(" ".join(matches))
    else:
        print("none")
        