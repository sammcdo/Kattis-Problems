names = [input() for i in range(int(input()))]

sortedNames = list(sorted(names))

if names == sortedNames:
    print("INCREASING")
elif names == sortedNames[::-1]:
    print("DECREASING")
else:
    print("NEITHER")