import bisect

try:
	while True:
		x = input()
		seq = [int(i) for i in input().split()]
		if not x:
			break
		dp = [-1] * len(seq)

		order = []
		order_inds = []

		last = -1
		for i in range(len(seq)):
			ins = bisect.bisect_left(order, seq[i])

			if ins:
				dp[i] = order_inds[ins-1]

			if ins == len(order):
				order.append(seq[i])
				order_inds.append(i)
				last = i
			else:
				order[ins] = seq[i]
				order_inds[ins] = i

		# print(dp)
		ans = []
		while last != -1:
			ans.append(last)
			last = dp[last]
		print(len(ans))
		print(*ans[::-1])
except:
	pass
