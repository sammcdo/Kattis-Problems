length = 0
for i in range(int(input())):
    if length == 0:
        length = int(input())
    else:
        length += int(input())-1

print(length)