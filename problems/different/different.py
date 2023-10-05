import sys

for line in sys.stdin:
    nums = [int(i) for i in line.split()]

    print(abs(nums[0] - nums[1]))
