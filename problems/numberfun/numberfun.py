n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())

    if a + b == c:
        print("Possible")
        continue
    elif a - b == c or b - a == c:
        print("Possible")
        continue
    elif a * b == c:
        print("Possible")
        continue
    elif a / b == c or b / a == c:
        print("Possible")
        continue
    else:
        print("Impossible")