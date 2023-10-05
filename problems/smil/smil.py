string = input() + "  "

for i in range(len(string)):
    char = string[i]
    if char == ":" or char == ";":
        if string[i+1] == ")":
            print(i)
        if string[i+1] == "-" and string[i+2] == ")":
            print(i)
