word = input()

letters = ["P", "E", "R"]

count = 0
for i in range(0, len(word)):
    if word[i] != letters[i%3]:
        count += 1

print(count)