b = 0
good = input() + " "

bad = input() + " "

sticky = set()

for g in good:
    while bad[b] != g:
        sticky.add(bad[b])
        b += 1
    b += 1



print("".join(sticky))
