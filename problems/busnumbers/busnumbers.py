n = int(input())

nums = list(map(int, input().split()))
nums.sort()

# first, group them
groups = []
group = []
for i, num in enumerate(nums):
    if group == []:
        group.append(num)
    elif num == group[-1] + 1:
        group.append(num)
    else:
        groups.append(group)
        group = [num]
if len(group):
    groups.append(group)

s = []
for group in groups:
    if len(group) > 2:
        s.append(f"{group[0]}-{group[-1]}")
    elif len(group) == 2:
        s.append(f"{group[0]} {group[-1]}")
    else:
        s.append(group[0])
print(*s)