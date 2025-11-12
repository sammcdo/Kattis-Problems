x = input()

i = 0
final = ""
while i < len(x):
    final += x[i]
    if x[i] in "aeiou":
        i += 2
    i += 1

print(final)