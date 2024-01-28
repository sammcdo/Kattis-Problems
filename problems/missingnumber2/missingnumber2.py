t = int(input())

for _ in range(t):
    s = input()
    opts = []
    
    # iterate every digit span (1...len(s))
    for span in range(1, min(len(s), 5) + 1):
        # We can assume the first number (or second in some cases) begins on the first index with no offset
        first = int(s[0:span])
        offset = span
        num = first
        strikes = 0
        lastStrikeNumber = -1
        throughS = False
        while True:
            num += 1
            strNum = str(num)
            match = s[offset:offset + len(strNum)]
            if str(num) == match:
                offset += len(strNum)
            else:
                lastStrikeNumber = num
                strikes += 1

            if offset >= len(s):
                throughS = True

            if throughS:
                if strikes == 1 and lastStrikeNumber != num:
                    opts.append(lastStrikeNumber)
                else:
                    opts.append(first - 1)
                    if lastStrikeNumber > 0:
                        opts.append(lastStrikeNumber)
                    else:
                        opts.append(num + 1)
                break
            if strikes == 2:
                break
    
    try:
        opts.remove(0)
    except:
        pass
    try:
        opts.remove(100000)
    except:
        pass
    print(len(opts))
    opts.sort()
    print(*opts)
