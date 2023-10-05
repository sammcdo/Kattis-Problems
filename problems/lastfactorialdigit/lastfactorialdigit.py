n = int(input())

for i in range(n):
    num = int(input())

    f = 1
    for j in range(2, num + 1):
        f *= j

    print(str(f)[-1])