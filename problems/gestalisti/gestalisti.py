names = set()

cmds = int(input())

for i in range(cmds):
    this = input().split()
    
    if this[0] == "+":
        names.add(this[1])
    
    elif this[0] == "-":
        if this[1] in names:
            names.remove(this[1])
    
    else:
        if this[1] in names:
            print("Jebb")
        else:
            print("Neibb")