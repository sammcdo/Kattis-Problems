import math
import sys

n = int(input())

heights = [int(i) for i in input().split()]

highest = -1

m = 0
for i in range(len(heights)):
	if heights[i] > m:
		m = heights[i]
		highest = i

heights = heights[:highest+1]
if len(heights) == 1:
	print(0)
	sys.exit()

least_slope = float('inf')
least_slope_ind = -1
for i in range(1, len(heights)):
	slope = (m-heights[-i-1])/(i)
	if slope < least_slope:
		least_slope = slope
		least_slope_ind = i

a = heights[0] + 4
a = math.ceil((m-heights[0]-4) / least_slope) - highest

b = (m-heights[0]-4)/(a+highest)

if a < 0:
	a = 0
	print(a)
elif b == least_slope:
	print(a+1)
else:
	print(a)
