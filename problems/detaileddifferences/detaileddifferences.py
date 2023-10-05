for i in range(int(input())):
    a = input()
    b = input()
    s = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            s += "."
        else:
            s += "*"
    print(a)
    print(b)
    print(s)
    print()