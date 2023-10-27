n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))

maxNums = max(nums)

found = False
for i in range(1, maxNums+1):
    if i not in nums:
        print(i)
        found = True
if not found:
    print("good job")