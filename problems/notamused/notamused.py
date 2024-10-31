i = 0
while True:
    i += 1
    try:
        input()
    except:
        break
    totals = {}
    entries = {}
    while True:
        cmd = input()
        if cmd == "CLOSE":
            break
        cmd = cmd.split()
        if cmd[0] == "ENTER":
            entries[cmd[1]] = int(cmd[2])
        else:
            t = int(cmd[2]) - entries[cmd[1]]
            del entries[cmd[1]]
            if cmd[1] not in totals:
                totals[cmd[1]] = 0
            totals[cmd[1]] += t * 0.1
            
    print("Day", i)
    for k,v in sorted(totals.items()):
        print("%s $%.2f" % (k,v))
    print()