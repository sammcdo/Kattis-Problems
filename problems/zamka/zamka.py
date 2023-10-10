start = int(input())
end = int(input())

target = int(input())

low = [9, 9, 9, 9, 9]
low_dec = 99999
high = [0]
high_dec = 0
for i in range(start, end + 1):
    s = [int(x) for x in str(i)]

    if sum(s) == target:
        if i < low_dec:
            low = s
            low_dec = i

        if i > high_dec:
            high = s
            high_dec = i

print(low_dec)
print(high_dec)