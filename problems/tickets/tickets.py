MAXLENGTH = 101

numberOfCases = int(input())

for i in range(numberOfCases):
    value_M, value_Z, r = map(int, input().split())
    # print(value_M, value_Z, r)
    M = [0]
    Z = [0]

    F = []
    S = []

    value_M -= 1

    # Decimal Representations
    n = 0
    temp_M = value_M
    temp_Z = value_Z
    while temp_M > 0:
        n += 1
        digit = int(temp_M % 10)
        M.append(digit)
        temp_M //= 10

        digit = int(temp_Z % 10)
        Z.append(digit)
        temp_Z //= 10
    # M.append(0)
    # Z.append(0)
    # n -= 1
    # print(M, Z, n)

    # Find F (aka not matching Z)
    for k in range(0, n+1):
        temp = 0
        for i in range(1, r+1):
            if (k-i) == -1:
                temp = temp + 1
            if (k-i) == 0:
                temp = temp+9
            if (k-i) > 0:
                temp = temp + 9 * F[k-i]
        F.append(temp)

    # print("F", F)

    # Find S (aka number that do not match and are smaller than M)
    powers = 10

    S.append(0)

    for i in range(1, r):
        suffix_M = value_M % powers
        S.append(suffix_M + 1)
        powers = powers * 10
    suffix_M = value_M % powers
    suffix_Z = value_Z % powers
    if suffix_M < suffix_Z:
        S.append(suffix_M + 1)
    else:
        S.append(suffix_M + 1 - 1)
    # print("S", S)

    for k in range(r+1, n+1):
        temp = 0
        if Z[k] > M[k]:
            temp = M[k]*F[k-1] + S[k-1]
        if Z[k] < M[k]:
            temp = (M[k]-1)*F[k-1] + S[k-1]
            for i in range(2,r+1):
                temp = temp + 9*F[k-i]
        if Z[k] == M[k]:
            temp = M[k]*F[k-1]
            for i in range(2, r+1):
                if Z[k-i+1] > M[k-i+1]:
                    temp = temp + M[k - i + 1] * F[k - i] + S[k - i]
                    break
                if Z[k-i+1] < M[k-i+1]:
                    temp = temp + (M[k - i + 1] - 1) * F[k - i] + S[k - i]
                    for j in range(i+1, r+1):
                        temp = temp + 9*F[k-j]
                    break
                if Z[k-i+1] == M[k-i+1]:
                    temp = temp + M[k-i+1]*F[k-i]
        S.append(temp)

    # print("NS", S)

    print(value_M+1-S[n])
    # print()


