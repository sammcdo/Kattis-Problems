isFinished = False
while not isFinished:
    progs = {}
    used = set()
    dups = set()
    last = ""
    while True:
        line = input()
        if line == "1":
            break
        if line == "0":
            isFinished = True
            break

        if line.isupper():
            progs[line] = set()
            last = line
        else:
            if line in used and line not in progs[last]:
                dups.add(line)
            else:
                progs[last].add(line)
                used.add(line)

    if not isFinished:
        out = []
        for k, v in progs.items():
            out.append([-len(v.difference(dups)), k])

        out.sort()

        for i in out:
            print(i[1], -i[0])