num = int(input())

l = []

for i in range(num):
    l.append(input())

for i in l[::-1]:
    print(i)