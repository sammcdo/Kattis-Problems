while True:
    pattern = input()
    if pattern == "0":
        break
    
    pattern = [int(i) for i in pattern.split()][1::]

    message = input()

    if len(message) % len(pattern) > 0:
        leftover = len(message) % len(pattern)
        message += " " * (len(pattern) - leftover)
    
    w = len(pattern)
    final = ""
    for i in range(0, len(message), w):
        chunk = message[i:i+w]
        # print(chunk)
        out = ""
        for j in pattern:
            out += chunk[j-1]
        final += out
    print('\'', final, '\'', sep="")