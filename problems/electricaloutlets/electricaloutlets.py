for i in range(int(input())):
    outlets = [int(i) for i in input().split()][1:]
    print(sum(outlets)-len(outlets)+1)
    