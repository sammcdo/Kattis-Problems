a = input()
b = input()

differences = 0
for i in range(4):
    if a[i] != b[i]:
        differences += 1

print(2 ** differences)