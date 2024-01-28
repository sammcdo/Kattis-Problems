s = input()

a = 0
b = 0

for c in s:
    if c in 'aeiou':
        a += 1
    if c in 'aeiouy':
        b += 1

print(a, b)