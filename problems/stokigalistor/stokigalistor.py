n = int(input())

nums = [int(i) for i in input().split()]

s = list(sorted(nums))

c = 0
for i in range(n):
    if nums[i] != s[i]:
        c += 1

print(c)