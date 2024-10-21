tiers = int(input())

slots = list(map(int, input().split()))

users = list(map(int, input().split()))

above = 0
zeros = 0
leftover = 0
score = 0
for i in range(tiers):
	# print(slots[i], users[i], above, zeros)
	# use above if space
	if above > 0:
		if above >= users[i]:
			above -= users[i]
			score += users[i]
			users[i] = 0
		else:
			users[i] -= above
			score += above
			above = 0
	# use previous zeroes for +1, -1 swap
	if zeros > 0 and users[i] > 0:
		if zeros >= users[i]:
			zeros -= users[i]
			score += users[i]
			leftover += users[i]
			users[i] = 0
		else:
			users[i] -= zeros
			score += zeros
			leftover += zeros
			zeros = 0
	# use also zero spaces
	newZeroes = 0
	if slots[i] > 0 and users[i] > 0:
		if slots[i] >= users[i]:
			slots[i] -= users[i]
			newZeroes += users[i]
			users[i] = 0
		else:
			users[i] -= slots[i]
			newZeroes += slots[i]
			slots[i] = 0
	# save for last as last resort
	if users[i] > 0:
		leftover += users[i]
	if slots[i] > 0:
		above += slots[i]
	zeros += newZeroes

score -= leftover

print(score)