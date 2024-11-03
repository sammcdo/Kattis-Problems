ip = input()

if "." in ip:
    ip = ".".join(ip.split(".")[::-1])
    print(ip+".in-addr.arpa.")
else:
    final = ""
    ip = ip.replace("::", ":X:")
    ip = ip.split(":")
    # print(ip)

    used = False
    for i, chunk in enumerate(ip):
        # print("c", chunk, "-", final)
        if chunk == "X":
            if not used:
                chunk = "0000"
                tomake = 8-len(ip)+2
                if i != 0:
                    tomake -= 1
                chunk = chunk*tomake
                # print(chunk)
                used = True
        else:
            # print("c", chunk, "-", final)
            while len(chunk) < 4:
                chunk = "0"+chunk
        final += chunk

    final = final[::-1]

    # print(final)

    f = ""
    for l in final:
        f += l+"."
    f += "ip6.arpa."

    print(f)