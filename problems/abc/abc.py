l = [int(i) for i in input().split()]

l.sort()

order = input()

for letter in order:
    if letter == "A":
        print(l[0], end=" ")
    if letter == "B":
        print(l[1], end=" ")
    if letter == "C":
        print(l[2], end=" ")
