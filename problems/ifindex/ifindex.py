nest = input()
inds = []
i = 0
stack = 0
while i < len(nest):
    if nest[i] == "i":
        inds.append(stack)
    if nest[i] == "{":
        stack += 1
    if nest[i] == "}":
        stack -= 1
    i += 1

if len(inds) == 0:
    print(-1)
else:
    inds.sort()
    print(inds[(len(inds)+1)//2 - 1])