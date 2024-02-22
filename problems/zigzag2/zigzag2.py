nums = [int(input()) for i in range(int(input()))]
new = [nums[0]]

for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        new.append(nums[i])

count = 1

if len(new) > 1 and new[0] != new[1]:
    count += 1


for i in range(2, len(new)):
    isUp = new[i] > new[i-1]
    wasUp = new[i-1] > new[i-2]
    if isUp != wasUp:
        count += 1

print(count)
