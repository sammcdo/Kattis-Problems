n = int(input())
p = int(input())

nums = list(map(int, input().split()))
nums.sort()

for i in range(p, n+p+1):
    if i not in nums:
        print(i)
        exit(0)