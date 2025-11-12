for i in range(int(input())):
    s = input()
    abbrv = input()
    flag = False
    for ch in abbrv:
        if ch not in s:
            flag = True
    if flag:
        print("NO")
    else:
        print("YES")