bestWord = "aaaaaaaaaaaaaaaaaaaaa"
for i in range(int(input())):
    word = input()

    if len(word) < 5:
        continue

    if len(set(word)) != len(word):
        continue

    if len(word) < len(bestWord):
        bestWord = word

    if len(word) == len(bestWord):
        bestWord = bestWord if bestWord > word else word

if len(bestWord) <= 20:
    print(bestWord)
else:
    print("Neibb")