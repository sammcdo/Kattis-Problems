n = int(input())

nums = [int(input()) for i in range(n)]

a = min(nums)
b = max(nums)

print(int(max(0,a-b/2)))