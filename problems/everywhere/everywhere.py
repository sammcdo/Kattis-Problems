for i in range(int(input())):
    a = int(input())
    l = []
    for i in range(a):
        l.append(input())
    print(len(set(l)))
    