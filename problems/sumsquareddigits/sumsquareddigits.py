for i in range(int(input())):
    a, base, num = [int(i) for i in input().split()]

    digits = []
    while num:
        digits.append(int(num % base) ** 2)
        num //= base

    print(a, sum(digits))