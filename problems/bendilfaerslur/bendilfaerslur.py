ip = input()

if "." in ip:
    ip = ".".join(ip.split(".")[::-1])
    print(ip+".in-addr.arpa.")
else:
    final = ""
    ip = ip.replace("::", ":X:")
    ip = ip.split(":")

    used = False
    for i, chunk in enumerate(ip):
        if chunk == "X":
            if not used:
                chunk = "0000"
                tomake = 8-len(ip)+2
                if i != 0:
                    tomake -= 1
                chunk = chunk*tomake
                used = True
        else:
            while len(chunk) < 4:
                chunk = "0"+chunk
        final += chunk

    final = final[::-1]

    f = ""
    for l in final:
        f += l+"."
    f += "ip6.arpa."

    print(f)