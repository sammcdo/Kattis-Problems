codes = {}

try:
    while True:
        line = input().split()

        if line[0] == "define":
            codes[line[2]] = int(line[1])
        else:
            a, b = line[1], line[3]
            op = line[2]

            if a not in codes or b not in codes:
                print("undefined")
                continue
            a = codes[a]
            b = codes[b]

            if op == ">":
                print("true" if a > b else "false")
            if op == "<":
                print("true" if a < b else "false")
            if op == "=":
                print("true" if a == b else "false")
except:
    pass