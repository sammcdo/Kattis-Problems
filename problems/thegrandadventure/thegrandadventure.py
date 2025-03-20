stack = []
for i in range(int(input())):
    stack = []
    for c in input():
        # print(c, stack, end=" ")
        if c == ".":
            continue
        if c in ["$", "|", "*"]:
            stack.append(c)
        if c == "b":
            if len(stack) and stack[-1] == "$":
                stack.pop(-1)
                continue
            else:
                stack=[1]
                break
        if c == "t":
            if len(stack) and stack[-1] == "|":
                stack.pop(-1)
                continue
            else:
                stack=[1]
                break
        if c == "j":
            if len(stack) and stack[-1] == "*":
                stack.pop(-1)
                continue
            else:
                stack=[1]
                break
    # print("here")
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
    # print(stack)