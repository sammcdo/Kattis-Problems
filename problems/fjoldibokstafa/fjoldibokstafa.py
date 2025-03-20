var = input()
x = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
c = 0
for l in var:
    if l in x:
        c += 1
print(c)