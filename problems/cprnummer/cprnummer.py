doubles = [4,3,2,7,6,5,4,3,2,1]

x = input().replace("-", "")
x = [int(i) for i in x]

nums = []
for i in range(len(doubles)):
    nums.append(x[i] * doubles[i])

print(int(sum(nums) % 11 == 0))