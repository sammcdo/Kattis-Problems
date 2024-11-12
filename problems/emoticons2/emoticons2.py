faces = [
    ":)",
    ":-)",
    ":-(",
    ";-)",
    "xD",
    "^_^",
    "-_-",
    "^o^",
    "^^;",
    "(..)",
]

symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def emojify(x):
    x = list(x)
    i = 0
    c = 0
    while i < len(x):
        for f in faces:
            if x[i:i+len(f)] == list(f):
                i += len(f)-1
                break
        c += 1
        i += 1
    return c

s = input()
shortest = float('inf')
longest = 0
for a in symbols:
    for b in symbols:
        c = emojify(s.replace(a,b))
        shortest = min(shortest, c)
        longest = max(longest, c)
    
print(shortest, longest)