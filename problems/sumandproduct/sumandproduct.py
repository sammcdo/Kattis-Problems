n = int(input())
nums = []

c = 0
for i in input().split():
    i = int(i)
    if i == 1:
        c += 1
    else:
        if c > 0:
            nums.append([1,c])
            c = 0
        nums.append([i,0])
if c > 0:
    nums.append([1,c])

# print(nums)

count = 0
i = 0
while i < len(nums):
    # print(i)
    s = 0
    p = 1

    for j in range(i, len(nums)):
        if nums[j][0] == 1:
            needs = p-s
            if needs > 0 and needs <= nums[j][1]:
                count += 1
            s += nums[j][1]
        else:
            s += nums[j][0]
            p *= nums[j][0]

            if s == p:
                count += 1

            if p > n*4:
                break
    if nums[i][0] == 1 and nums[i][1] > 1:
        nums[i][1] -= 1
        i -= 1
    i += 1
print(count - n)