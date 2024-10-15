sentence = input()

secret = ""
for word in sentence.split():
    # print(word)
    x = ""
    found = True
    for l in word:
        if not l.isalpha():
            continue
        if l == "u":
            x += "1"
        elif l == "m":
            x += "0"
        else:
            found = False
            break
    if found:
        secret += x


res = ""
for i in range(7, len(secret)+1, 7):
    this = secret[i-7:i]
    # print(this)
    char = int(this, base=2)
    char = chr(char)
    # print(char)
    res += char


print(res)