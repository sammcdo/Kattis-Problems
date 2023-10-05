for i in range(int(input())):
    days, months = input().split()
    monthDays = input().split()

    count = 0
    sumDays = 0

    for i in monthDays:
        if int(i) >= 13:
            if (sumDays+13) % 7 == 6:
                count += 1
        sumDays += int(i)

    # print(days, months)
    # print(monthDays)

    print(count)