a = int(input())

l = [int(input()) for i in range(a)][::-1]

for i in l:
    print(i)