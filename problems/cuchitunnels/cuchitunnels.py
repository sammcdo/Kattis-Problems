n = int(input())
nums = list(map(int, input().split()))
a = 2
for num in nums:
    if a <= 0:
        print('NO')
        quit()
    a += num - 2
if a == 0:
    print('YES')
else:
    print('NO')