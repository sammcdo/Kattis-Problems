def lis(nums):
   import bisect
   n = len(nums)
   ans = [nums[0]]
   for i in range(1, n):
       if nums[i] > ans[-1]:
           ans.append(nums[i])
       else:
           x = bisect.bisect_left(ans, nums[i])
           ans[x] = nums[i]
   return len(ans)

word = input()
correct = "abcdefghijklmnopqrstuvwxyz"

print(26-lis(word))