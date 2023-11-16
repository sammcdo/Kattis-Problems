l, w = map(int, input().split())


letters = "abcdefghijklmnopqrstuvwxyz"

count = 0
word = []

for x in range(l):
    word.append('a')

count = l

if count == w:
    print("".join(word))
    exit()
if count > w:
    print("impossible")
    exit()

while True:
    shouldExit = False
    found = False
    for x in range(l):
        n = letters.index(word[x])+1
        if n == 26:
            shouldExit = True
            break
        word[x] = letters[n]
        count += 1

        if count == w:
            print("".join(word))
            shouldExit = True
            found = True
            break

        if n == 25 and x == 25:
            shouldExit = True
            break

    if shouldExit:
        if not found:
            print("impossible")
        break