d = {
    "clank":"a",
    "bong":"b",
    "click":"c",
    "tap":"d",
    "poing":"e",
    "clonk":"f",
    "clack":"g",
    "ping":"h",
    "tip":"i",
    "cloing":"j",
    "tic":"k",
    "cling":"l",
    "bing":"m",
    "pong":"n",
    "clang":"o",
    "pang":"p",
    "clong":"q",
    "tac":"r",
    "boing":"s",
    "boink":"t",
    "cloink":"u",
    "rattle":"v",
    "clock":"w",
    "toc":"x",
    "clink":"y",
    "tuc":"z",
    "whack":" ",
}

word = ""
caps = False
for i in range(int(input())):
    letter = input()

    if letter in d:
        if caps:
            word += d[letter].upper()
        else:
            word += d[letter].lower()
    else:
        if letter in ["bump", "dink", "thumb"]:
            caps = not caps
        if letter == "pop":
            word = word[0:-1]

print(word)