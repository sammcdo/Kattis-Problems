input()

nums = [int(i) for i in input().split()]
nums.sort()

total = 0
for i in range(1, len(nums)):
    total += (nums[i-1] - nums[i]) ** 2

print(total)